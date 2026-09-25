# SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Fast packaging checks; model behavior is evaluated separately."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_manifest_and_marketplace_resolve_the_same_plugin(self):
        manifest = json.loads((ROOT / "plugin.json").read_text())
        marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
        self.assertEqual(manifest["$schema"], "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(len(marketplace["plugins"]), 1)
        entry = marketplace["plugins"][0]
        self.assertEqual(entry["name"], manifest["name"])
        self.assertEqual(entry["source"], {"source": "local", "path": "./"})
        self.assertEqual(entry["policy"]["installation"], "AVAILABLE")

    def test_skill_activation_metadata_and_local_links(self):
        skills = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertTrue(skills)
        for skill in skills:
            text = skill.read_text()
            self.assertTrue(text.startswith("---\n"), skill)
            frontmatter = text.split("---\n", 2)[1]
            self.assertEqual(re.search(r"(?m)^name: ([a-z0-9-]+)$", frontmatter).group(1), skill.parent.name)
            self.assertRegex(frontmatter, r"(?m)^description: .{40,}")
        for file in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", file.read_text()):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((file.parent / target.split("#", 1)[0]).is_file(), (file, target))

    def test_review_publication_requires_express_authorization(self):
        text = (ROOT / "skills/review-pull-request/SKILL.md").read_text()
        self.assertIn("Do not post comments or reviews", text)
        self.assertIn("expressly authorize", text)
        self.assertIn("Recheck the target SHA and line anchors", text)

    def test_synthetic_answers_anchor_to_changed_lines(self):
        for fixture in (ROOT / "evaluations/fixtures").glob("*.json"):
            case = json.loads(fixture.read_text())
            self.assertTrue(case["task"] and case["diff"])
            hunk = re.search(r"(?m)^@@ -\d+,\d+ \+(\d+),(\d+) @@$", case["diff"])
            self.assertIsNotNone(hunk, fixture)
            line = int(hunk.group(1))
            changed = set()
            for content in case["diff"].split("\n")[4:]:
                if content.startswith("+"):
                    changed.add(line)
                    line += 1
                elif content.startswith(" "):
                    line += 1
            self.assertEqual(line, int(hunk.group(1)) + int(hunk.group(2)), fixture)
            for finding in case["expected"]:
                self.assertIn(f"b/{finding['path']}", case["diff"], fixture)
                self.assertIn(finding["line"], changed, fixture)


if __name__ == "__main__":
    unittest.main()
