# 🧠 skill-vault — AI 方法论技能库

把已安装的 27 个 AI 方法论技能做成一个**带数据库的可视化网页**：每个技能有小白版大白话解释、使用场景、生活化例子、原文金句、方法论骨架、书中案例、可执行步骤、边界，另有独立的名词术语表。响应式设计，手机可直接访问。

## 📁 项目结构

```
skill-vault/
├── skills_src/           # 原始 SKILL.md 源文件（35 个技能，只读参考）
│   └── <skill-id>/SKILL.md   # ★ 规范：每个技能一个目录，直接放在 skills_src/ 下（目录名 = 技能 id）
├── content/              # 内容包 JSON（每个技能一个：大白话解释/场景/案例…）
├── scripts/
│   ├── seed.py           # ★ 主构建脚本：建库 + 导入 + 导出
│   └── verify.py         # 校验脚本（查库 + 查导出 JSON）
├── db/
│   └── skills.db         # ★ SQLite 数据库（主数据，三张表）
└── web/                  # ★ 前端静态站点（可直接部署）
    ├── index.html
    ├── app.js
    ├── style.css
    └── data/skills.json  # 前端数据源（由 seed.py 从数据库导出）
```

**数据流**：`skills_src/*.md + content/*.json → seed.py → db/skills.db → web/data/skills.json → 网页`

## 🗄️ 数据库（db/skills.db）

| 表 | 说明 | 关键字段 |
|---|---|---|
| `categories` | 分类 | id, name, icon |
| `skills` | 技能主表 | id, name_cn, category_id, source, plain(大白话), use_cases, example, quote, core, cases, steps, boundary, related |
| `terms` | 名词术语 | term, plain(大白话解释), skill_id |

> 网页不直接连数据库——`seed.py` 把数据导出成 `web/data/skills.json`（纯静态，任何托管都能跑，无需后端）。

## ➕ 以后加新技能（三步）

1. **源文件**：把技能目录放到 `skills_src/<技能id>/SKILL.md`（必须直接放 `skills_src/` 下，不要再多套一层目录）
2. **内容包**：把新技能的 JSON 放进 `content/<新id>.json`（字段结构参考 `content/one-second-rule.json`；也可以让我从 SKILL.md 自动生成）
3. **映射**：在 `scripts/seed.py` 的 `SKILL_META` 字典里加一行：`"新id": ("分类id", "来源说明")`，然后 `python scripts/seed.py`

> 相关技能（related）解析支持两种 SKILL.md 写法：正文的 `**id** (relation)` 格式，以及 yaml 块里的 `related_skills: [a, b]` / `- slug: a` 格式。

分类 id：`eval` 评估与决策 / `exec` 流程与执行 / `data` 数据与技术 / `strat` 战略与转型 / `org` 组织与团队 / `meta` 元技能工具（也可在 `CATEGORIES` 里新增分类）。

## 🖥️ 本地预览

```bash
cd web
python -m http.server 8000
# 浏览器打开 http://localhost:8000
```

## 📱 手机访问（同一 WiFi 局域网）

```bash
python -m http.server 8765 --bind 0.0.0.0 --directory web
# 先查电脑 IP：ipconfig（如 192.168.1.5）
# 手机浏览器打开 http://192.168.1.5:8765
```

## 🌍 部署到公网（任选其一，均无需后端）

- **GitHub Pages / Cloudflare Pages / Netlify / Vercel**：把 `web/` 整个目录上传即可
- 数据更新流程：改数据库 → `python scripts/seed.py` → 重新上传 `web/data/skills.json`

## 🔧 常见操作

| 需求 | 命令 |
|---|---|
| 重建数据库 + 导出前端数据 | `python scripts/seed.py` |
| 校验数据完整性 | `python scripts/verify.py` |
| 改某个技能的大白话解释 | 编辑 `content/<id>.json` 后重建 |
