#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skill-vault 数据构建脚本
=======================
1. 读取 content/*.json（27 个 skill 的内容包）
2. 从 skills_src/*/SKILL.md 提取官方描述(short_desc)与相关技能(related)
3. 构建 SQLite 数据库 db/skills.db（categories / skills / terms 三张表）
4. 导出 web/data/skills.json 供前端使用

扩展方式：以后新增 skill 时，把内容包 JSON 放进 content/ 目录
（id 与 SKILL.md 的 name 一致），重新运行本脚本即可增量入库。
"""

import json
import os
import re
import sqlite3

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE, "content")
SRC_DIR = os.path.join(BASE, "skills_src")
DB_DIR = os.path.join(BASE, "db")
DB_PATH = os.path.join(DB_DIR, "skills.db")
WEB_DATA_PATH = os.path.join(BASE, "web", "data", "skills.json")

# ---------- 分类定义（id 稳定，扩展时只加不改） ----------
CATEGORIES = [
    {"id": "eval",  "name": "评估与决策", "icon": "🔍", "description": "能不能做 / 值不值得做"},
    {"id": "exec",  "name": "流程与执行", "icon": "⚙️", "description": "怎么做 / 怎么落地"},
    {"id": "data",  "name": "数据与技术", "icon": "📊", "description": "数据基础设施"},
    {"id": "strat", "name": "战略与转型", "icon": "🚀", "description": "组织层面怎么走"},
    {"id": "org",   "name": "组织与团队", "icon": "👥", "description": "人 / 协作"},
    {"id": "meta",  "name": "元技能 / 工具", "icon": "🧰", "description": "工具类技能"},
    {"id": "loop",  "name": "循环工程", "icon": "⚡", "description": "设计 AI 自动化循环系统（Loop Engineering）"},
]
CATEGORY_NAMES = {c["id"]: c["name"] for c in CATEGORIES}

SOURCE_AI = "吴恩达《AI for Everyone》· kangarooking/ai-for-everyone-skill 蒸馏"
SOURCE_CANGJIE = "kangarooking/cangjie-skill（拆书蒸馏元技能）"
SOURCE_FIND = "DSH 内置技能（skills.sh 生态）"
SOURCE_LOOP = "kangarooking/loop-engineering-skill（Loop Engineering 视频合集蒸馏）"

# ---------- skill -> (分类, 来源) 映射（扩展时在此追加一行） ----------
SKILL_META = {
    "one-second-rule": ("eval", SOURCE_AI),
    "ab-mapping": ("eval", SOURCE_AI),
    "ml-feasibility": ("eval", SOURCE_AI),
    "ml-vs-ds": ("eval", SOURCE_AI),
    "build-vs-buy": ("eval", SOURCE_AI),
    "three-value-drivers": ("eval", SOURCE_AI),
    "dont-acquire-for-data": ("eval", SOURCE_AI),
    "triple-due-diligence": ("eval", SOURCE_AI),
    "ai-project-lifecycle": ("exec", SOURCE_AI),
    "ml-workflow": ("exec", SOURCE_AI),
    "ai-pipeline": ("exec", SOURCE_AI),
    "train-test-split": ("exec", SOURCE_AI),
    "iterate-not-perfect": ("exec", SOURCE_AI),
    "dont-wait-perfect-data": ("exec", SOURCE_AI),
    "statistical-acceptance": ("exec", SOURCE_AI),
    "automate-task": ("exec", SOURCE_AI),
    "data-flywheel": ("data", SOURCE_AI),
    "unified-data-warehouse": ("data", SOURCE_AI),
    "ai-strategy-moat": ("strat", SOURCE_AI),
    "ai-transformation-playbook": ("strat", SOURCE_AI),
    "pilot-momentum-flywheel": ("strat", SOURCE_AI),
    "start-small-find-partner": ("strat", SOURCE_AI),
    "cross-functional-brainstorming": ("strat", SOURCE_AI),
    "ai-team-building": ("org", SOURCE_AI),
    "role-tiered-training": ("org", SOURCE_AI),
    "cangjie-skill": ("meta", SOURCE_CANGJIE),
    "find-skills": ("meta", SOURCE_FIND),
    "loop-three-elements": ("loop", SOURCE_LOOP),
    "loop-worthiness-test": ("loop", SOURCE_LOOP),
    "goal-verification": ("loop", SOURCE_LOOP),
    "loop-5plus1-architecture": ("loop", SOURCE_LOOP),
    "loop-build-path": ("loop", SOURCE_LOOP),
    "maker-checker": ("loop", SOURCE_LOOP),
    "comprehension-gap": ("loop", SOURCE_LOOP),
    "three-stage-evolution": ("loop", SOURCE_LOOP),
}


def parse_skill_md(skill_id):
    """从 SKILL.md 提取官方描述与相关技能列表。"""
    path = os.path.join(SRC_DIR, skill_id, "SKILL.md")
    if not os.path.exists(path):
        return "", []
    with open(path, encoding="utf-8") as f:
        text = f.read()
    desc = ""
    m = re.search(r"^description:\s*\|?\s*(.+)$", text, re.MULTILINE)
    if m:
        desc = m.group(1).strip()
        # 取 frontmatter 内 description 块完整内容
        block = re.search(r"(?s)^description:\s*(\|?\s*.*?)^\w", text, re.MULTILINE)
        if block:
            lines = []
            for ln in block.group(1).splitlines():
                ln = re.sub(r"^\s+", "", ln)
                lines.append(ln)
            desc = "\n".join(lines).strip()
    related = re.findall(r"\*\*([a-z0-9-]+)\*\*\s*\(([a-z-]+)\)", text)
    related = [{"id": rid, "relation": rel} for rid, rel in related]
    return desc, related


def normalize_content(c):
    """内容包规范化：core/plain/example/quote 等字段必须是字符串，
    若子代理写成列表则用换行连接（向前兼容）。"""
    for k in ("name_cn", "plain", "example", "quote", "core"):
        v = c.get(k)
        if isinstance(v, list):
            c[k] = "\n".join(str(x) for x in v)
    return c


def main():
    # 1. 读取全部内容包
    contents = {}
    for fn in sorted(os.listdir(CONTENT_DIR)):
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(CONTENT_DIR, fn), encoding="utf-8") as f:
            c = json.load(f)
        contents[c["id"]] = normalize_content(c)

    missing = [sid for sid in SKILL_META if sid not in contents]
    if missing:
        print(f"[WARN] 缺少内容包: {missing}")

    # 2. 建库
    os.makedirs(DB_DIR, exist_ok=True)
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE categories (
            id          TEXT PRIMARY KEY,
            name        TEXT NOT NULL,
            icon        TEXT,
            description TEXT
        );
        CREATE TABLE skills (
            id          TEXT PRIMARY KEY,
            name        TEXT NOT NULL,
            name_cn     TEXT,
            category_id TEXT REFERENCES categories(id),
            source      TEXT,
            short_desc  TEXT,
            plain       TEXT,
            use_cases   TEXT,
            example     TEXT,
            quote       TEXT,
            core        TEXT,
            cases       TEXT,
            steps       TEXT,
            boundary    TEXT,
            related     TEXT,
            sort_order  INTEGER
        );
        CREATE TABLE terms (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            term    TEXT NOT NULL,
            plain   TEXT NOT NULL,
            skill_id TEXT REFERENCES skills(id)
        );
        CREATE INDEX idx_terms_term ON terms(term);
        """
    )

    for c in CATEGORIES:
        cur.execute(
            "INSERT INTO categories (id, name, icon, description) VALUES (?,?,?,?)",
            (c["id"], c["name"], c["icon"], c["description"]),
        )

    exported_skills = []
    term_index = {}  # term -> {plain, skills:[]}
    for order, (sid, (cat, source)) in enumerate(SKILL_META.items()):
        c = contents.get(sid)
        if c is None:
            continue
        desc, related = parse_skill_md(sid)
        cur.execute(
            """INSERT INTO skills
               (id, name, name_cn, category_id, source, short_desc, plain,
                use_cases, example, quote, core, cases, steps, boundary, related, sort_order)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                sid, sid, c.get("name_cn", ""), cat, source, desc,
                c.get("plain", ""),
                json.dumps(c.get("use_cases", []), ensure_ascii=False),
                c.get("example", ""),
                c.get("quote", ""),
                c.get("core", ""),
                json.dumps(c.get("cases", []), ensure_ascii=False),
                json.dumps(c.get("steps", []), ensure_ascii=False),
                json.dumps(c.get("boundary", []), ensure_ascii=False),
                json.dumps(related, ensure_ascii=False),
                order,
            ),
        )
        for t in c.get("terms", []):
            cur.execute(
                "INSERT INTO terms (term, plain, skill_id) VALUES (?,?,?)",
                (t["term"], t["plain"], sid),
            )
            key = t["term"]
            if key not in term_index:
                term_index[key] = {"term": key, "plain": t["plain"], "skills": []}
            if sid not in term_index[key]["skills"]:
                term_index[key]["skills"].append(sid)
        exported_skills.append(
            {
                "id": sid,
                "name": sid,
                "name_cn": c.get("name_cn", ""),
                "category": cat,
                "category_name": CATEGORY_NAMES[cat],
                "source": source,
                "short_desc": desc,
                "plain": c.get("plain", ""),
                "use_cases": c.get("use_cases", []),
                "example": c.get("example", ""),
                "quote": c.get("quote", ""),
                "core": c.get("core", ""),
                "cases": c.get("cases", []),
                "steps": c.get("steps", []),
                "boundary": c.get("boundary", []),
                "related": related,
            }
        )

    conn.commit()
    print(f"[OK] SQLite: {len(exported_skills)} skills, {len(term_index)} terms -> {DB_PATH}")

    # 3. 导出前端 JSON
    payload = {
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "categories": CATEGORIES,
        "skills": exported_skills,
        "terms": [{"term": k, "plain": v["plain"], "skills": v["skills"]} for k, v in term_index.items()],
    }
    os.makedirs(os.path.dirname(WEB_DATA_PATH), exist_ok=True)
    with open(WEB_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    print(f"[OK] Web data -> {WEB_DATA_PATH}")
    conn.close()


if __name__ == "__main__":
    main()
