# -*- coding: utf-8 -*-
import sqlite3, json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

conn = sqlite3.connect(r"G:\mywork\skill-vault\db\skills.db")
print("== categories ==")
for r in conn.execute("SELECT id, name FROM categories ORDER BY rowid"):
    print(" ", r)
print("== skills per category ==")
for r in conn.execute("SELECT category_id, COUNT(*) FROM skills GROUP BY category_id"):
    print(" ", r)
print("== sample skill ==")
row = conn.execute(
    "SELECT id, name_cn, source, substr(plain,1,28) FROM skills WHERE id='ml-feasibility'"
).fetchone()
print(" ", row)
print("== terms sample ==")
for r in conn.execute("SELECT term, skill_id FROM terms LIMIT 3"):
    print(" ", r)
conn.close()

d = json.load(open(r"G:\mywork\skill-vault\web\data\skills.json", encoding="utf-8"))
print("== web json ==")
print("  skills:", len(d["skills"]), "terms:", len(d["terms"]), "categories:", len(d["categories"]))
print("  first skill keys:", sorted(d["skills"][0].keys()))
print("  all skills:", [s["id"] for s in d["skills"]])
