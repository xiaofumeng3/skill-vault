#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skill-vault 数据构建脚本
=======================
1. 读取 content/*.json（60 个 skill 的内容包）
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
    {"id": "coding", "name": "编程智能体", "icon": "🧑‍💻", "description": "需求 / 代码 / 测试 / 审查"},
    {"id": "meta",  "name": "元技能 / 工具", "icon": "🧰", "description": "工具类技能"},
    {"id": "loop",  "name": "循环工程", "icon": "⚡", "description": "设计 AI 自动化循环系统（Loop Engineering）"},
]
CATEGORY_NAMES = {c["id"]: c["name"] for c in CATEGORIES}

SOURCE_AI = "吴恩达《AI for Everyone》· kangarooking/ai-for-everyone-skill 蒸馏"
SOURCE_CANGJIE = "kangarooking/cangjie-skill（拆书蒸馏元技能）"
SOURCE_FIND = "DSH 内置技能（skills.sh 生态）"
SOURCE_LOOP = "kangarooking/loop-engineering-skill（Loop Engineering 视频合集蒸馏）"
SOURCE_MATT = "mattpocock/skills（固定快照）"
MATT_REPO_URL = "https://github.com/mattpocock/skills"
MATT_COMMIT = "9c9f36ccd3995266cd675468af71639c8dde1ec5"
MATT_SNAPSHOT_DATE = "2026-08-19"

MATT_SOURCE_PATHS = {
    "ask-matt": "skills/engineering/ask-matt",
    "code-review": "skills/engineering/code-review",
    "codebase-design": "skills/engineering/codebase-design",
    "diagnosing-bugs": "skills/engineering/diagnosing-bugs",
    "domain-modeling": "skills/engineering/domain-modeling",
    "grill-with-docs": "skills/engineering/grill-with-docs",
    "implement": "skills/engineering/implement",
    "improve-codebase-architecture": "skills/engineering/improve-codebase-architecture",
    "prototype": "skills/engineering/prototype",
    "research": "skills/engineering/research",
    "resolving-merge-conflicts": "skills/engineering/resolving-merge-conflicts",
    "setup-matt-pocock-skills": "skills/engineering/setup-matt-pocock-skills",
    "tdd": "skills/engineering/tdd",
    "to-spec": "skills/engineering/to-spec",
    "to-tickets": "skills/engineering/to-tickets",
    "triage": "skills/engineering/triage",
    "wayfinder": "skills/engineering/wayfinder",
    "wizard": "skills/engineering/wizard",
    "grill-me": "skills/productivity/grill-me",
    "grilling": "skills/productivity/grilling",
    "handoff": "skills/productivity/handoff",
    "teach": "skills/productivity/teach",
    "to-questionnaire": "skills/productivity/to-questionnaire",
    "wait-what": "skills/productivity/wait-what",
    "writing-for-agents": "skills/productivity/writing-for-agents",
}

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
    "setup-matt-pocock-skills": ("coding", SOURCE_MATT),
    "ask-matt": ("coding", SOURCE_MATT),
    "grill-me": ("coding", SOURCE_MATT),
    "grill-with-docs": ("coding", SOURCE_MATT),
    "domain-modeling": ("coding", SOURCE_MATT),
    "to-spec": ("coding", SOURCE_MATT),
    "to-tickets": ("coding", SOURCE_MATT),
    "wayfinder": ("coding", SOURCE_MATT),
    "triage": ("coding", SOURCE_MATT),
    "research": ("coding", SOURCE_MATT),
    "prototype": ("coding", SOURCE_MATT),
    "codebase-design": ("coding", SOURCE_MATT),
    "implement": ("coding", SOURCE_MATT),
    "tdd": ("coding", SOURCE_MATT),
    "diagnosing-bugs": ("coding", SOURCE_MATT),
    "resolving-merge-conflicts": ("coding", SOURCE_MATT),
    "improve-codebase-architecture": ("coding", SOURCE_MATT),
    "code-review": ("coding", SOURCE_MATT),
    "to-questionnaire": ("coding", SOURCE_MATT),
    "wizard": ("coding", SOURCE_MATT),
    "teach": ("coding", SOURCE_MATT),
    "wait-what": ("coding", SOURCE_MATT),
    "handoff": ("coding", SOURCE_MATT),
    "writing-for-agents": ("coding", SOURCE_MATT),
    "grilling": ("coding", SOURCE_MATT),
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
    related = []
    seen = set()
    # 1) 正文里 **id** (relation) 格式（如 AI for Everyone 系列的"相关 skills"段落）
    for rid, rel in re.findall(r"\*\*([a-z0-9-]+)\*\*\s*\(([a-z-]+)\)", text):
        if rid not in seen:
            seen.add(rid)
            related.append({"id": rid, "relation": rel})
    # 2) yaml 块（frontmatter 或 ```yaml 代码块）里的 related_skills：
    #    内联数组 [a, b] 或列表 - slug: a
    fm = re.search(r"(?s)^---\r?\n(.*?)\r?\n---", text)
    blocks = re.findall(r"(?s)```yaml\r?\n(.*?)```", text)
    if fm:
        blocks.append(fm.group(1))
    for block in blocks:
        for mm in re.finditer(r"(?m)^related_skills:\s*\[([^\]]*)\]", block):
            for rid in re.findall(r"[a-z0-9-]+", mm.group(1)):
                if rid not in seen:
                    seen.add(rid)
                    related.append({"id": rid, "relation": "related"})
        for mm in re.finditer(r"(?m)^\s*-\s*slug:\s*([a-z0-9-]+)", block):
            rid = mm.group(1)
            if rid not in seen:
                seen.add(rid)
                related.append({"id": rid, "relation": "related"})
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
            content_type TEXT,
            role        TEXT,
            source_url  TEXT,
            source_file_url TEXT,
            snapshot_commit TEXT,
            snapshot_date TEXT,
            plain       TEXT,
            use_cases   TEXT,
            example     TEXT,
            quote       TEXT,
            core        TEXT,
            cases       TEXT,
            steps       TEXT,
            boundary    TEXT,
            related     TEXT,
            prompt_examples TEXT,
            recommended_with TEXT,
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
               (id, name, name_cn, category_id, source, short_desc,
                content_type, role, source_url, source_file_url, snapshot_commit,
                snapshot_date,
                plain, use_cases, example, quote, core, cases, steps, boundary,
                related, prompt_examples, recommended_with, sort_order)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                sid, sid, c.get("name_cn", ""), cat, source, desc,
                c.get("content_type", "methodology"),
                c.get("role", "内容 Skill"),
                MATT_REPO_URL if sid in MATT_SOURCE_PATHS else "",
                (f"{MATT_REPO_URL}/blob/{MATT_COMMIT}/{MATT_SOURCE_PATHS[sid]}/SKILL.md"
                 if sid in MATT_SOURCE_PATHS else ""),
                MATT_COMMIT if sid in MATT_SOURCE_PATHS else "",
                MATT_SNAPSHOT_DATE if sid in MATT_SOURCE_PATHS else "",
                c.get("plain", ""),
                json.dumps(c.get("use_cases", []), ensure_ascii=False),
                c.get("example", ""),
                c.get("quote", ""),
                c.get("core", ""),
                json.dumps(c.get("cases", []), ensure_ascii=False),
                json.dumps(c.get("steps", []), ensure_ascii=False),
                json.dumps(c.get("boundary", []), ensure_ascii=False),
                json.dumps(related, ensure_ascii=False),
                json.dumps(c.get("prompt_examples", []), ensure_ascii=False),
                json.dumps(c.get("recommended_with", []), ensure_ascii=False),
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
                "content_type": c.get("content_type", "methodology"),
                "role": c.get("role", "内容 Skill"),
                "source_url": MATT_REPO_URL if sid in MATT_SOURCE_PATHS else "",
                "source_file_url": (f"{MATT_REPO_URL}/blob/{MATT_COMMIT}/{MATT_SOURCE_PATHS[sid]}/SKILL.md"
                                    if sid in MATT_SOURCE_PATHS else ""),
                "snapshot_commit": MATT_COMMIT if sid in MATT_SOURCE_PATHS else "",
                "snapshot_date": MATT_SNAPSHOT_DATE if sid in MATT_SOURCE_PATHS else "",
                "plain": c.get("plain", ""),
                "use_cases": c.get("use_cases", []),
                "example": c.get("example", ""),
                "quote": c.get("quote", ""),
                "core": c.get("core", ""),
                "cases": c.get("cases", []),
                "steps": c.get("steps", []),
                "boundary": c.get("boundary", []),
                "related": related,
                "prompt_examples": c.get("prompt_examples", []),
                "recommended_with": c.get("recommended_with", []),
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
