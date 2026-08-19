#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Behavior checks for the mattpocock coding-agent skill collection."""

import json
import os
import unittest


BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE, "content")
SRC_DIR = os.path.join(BASE, "skills_src")
WEB_DATA = os.path.join(BASE, "web", "data", "skills.json")
APP_JS = os.path.join(BASE, "web", "app.js")

CODING_SKILLS = [
    "setup-matt-pocock-skills",
    "ask-matt",
    "grill-me",
    "grill-with-docs",
    "domain-modeling",
    "to-spec",
    "to-tickets",
    "wayfinder",
    "triage",
    "research",
    "prototype",
    "codebase-design",
    "implement",
    "tdd",
    "diagnosing-bugs",
    "resolving-merge-conflicts",
    "improve-codebase-architecture",
    "code-review",
    "to-questionnaire",
    "wizard",
    "teach",
    "wait-what",
    "handoff",
    "writing-for-agents",
    "grilling",
]


class CodingSkillContentTests(unittest.TestCase):
    def test_all_25_source_directories_are_complete_enough_to_use(self):
        for skill_id in CODING_SKILLS:
            with self.subTest(skill=skill_id):
                skill_file = os.path.join(SRC_DIR, skill_id, "SKILL.md")
                self.assertTrue(os.path.isfile(skill_file), skill_file)

    def test_all_25_content_packs_have_the_public_display_contract(self):
        for skill_id in CODING_SKILLS:
            with self.subTest(skill=skill_id):
                path = os.path.join(CONTENT_DIR, f"{skill_id}.json")
                self.assertTrue(os.path.isfile(path), path)
                with open(path, encoding="utf-8") as f:
                    item = json.load(f)
                self.assertEqual(item["id"], skill_id)
                self.assertEqual(item["content_type"], "coding-agent")
                self.assertIn(item["role"], {"入口 Skill", "核心 Skill", "底层支持"})
                for field in ("name_cn", "plain", "example", "quote", "core"):
                    self.assertTrue(item.get(field), f"{skill_id}.{field}")
                for field in ("use_cases", "cases", "steps", "boundary", "terms"):
                    self.assertTrue(item.get(field), f"{skill_id}.{field}")
                prompts = item.get("prompt_examples", [])
                self.assertEqual(len(prompts), 2, f"{skill_id}.prompt_examples")
                self.assertEqual(
                    {p.get("title") for p in prompts}, {"快速调用", "完整调用"}
                )
                self.assertTrue(item.get("recommended_with"), f"{skill_id}.recommended_with")

    def test_export_exposes_category_roles_prompts_and_fixed_source(self):
        with open(WEB_DATA, encoding="utf-8") as f:
            data = json.load(f)
        categories = {c["id"] for c in data["categories"]}
        self.assertIn("coding", categories)
        self.assertEqual(len(data["skills"]), 60)
        by_id = {s["id"]: s for s in data["skills"]}
        for skill_id in CODING_SKILLS:
            with self.subTest(skill=skill_id):
                item = by_id[skill_id]
                self.assertEqual(item["category"], "coding")
                self.assertEqual(item["content_type"], "coding-agent")
                self.assertEqual(
                    item["snapshot_commit"],
                    "9c9f36ccd3995266cd675468af71639c8dde1ec5",
                )
                self.assertEqual(item["snapshot_date"], "2026-08-19")
                self.assertTrue(item["source_url"].startswith("https://github.com/"))
                self.assertIn(item["snapshot_commit"], item["source_file_url"])

    def test_frontend_has_dynamic_coding_skill_sections(self):
        with open(APP_JS, encoding="utf-8") as f:
            source = f.read()
        for required in (
            "content_type",
            "核心原则",
            "工作机制",
            "开发场景",
            "复制调用示例",
            "推荐组合",
            "source_file_url",
            "snapshot_date",
            "s.snapshot_commit",
        ):
            self.assertIn(required, source)


if __name__ == "__main__":
    unittest.main()
