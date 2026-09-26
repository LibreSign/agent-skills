# SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Fast packaging checks; model behavior is evaluated separately."""

import hashlib
import json
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_complete_unmodified_root_license(self):
        # Full text from github/choosealicense.com/_licenses/agpl-3.0.txt
        # (excluding its Jekyll frontmatter), not a project-specific summary.
        root_license = (ROOT / "LICENSE").read_bytes()
        reuse_license = (ROOT / "LICENSES/AGPL-3.0-or-later.txt").read_bytes()
        self.assertEqual(root_license, reuse_license)
        self.assertEqual(
            hashlib.sha256(root_license).hexdigest(),
            "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
        )

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

    def test_every_skill_loads_shared_trust_boundary(self):
        policy = ROOT / "references/untrusted-input.md"
        policy_text = policy.read_text()
        for required in ("lower-trust", "trusted base revision", "credentials", "permissions", "interacting person"):
            self.assertIn(required, policy_text)
        skills = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertTrue(skills)
        for skill in skills:
            relative = os.path.relpath(policy, skill.parent)
            text = skill.read_text()
            self.assertIn(f"]({relative})", text, skill)
            self.assertRegex(text, r"(?i)before (reading|processing).*content", skill)

    def test_paid_model_evaluation_runs_only_from_main(self):
        workflow = (ROOT / ".github/workflows/model-evals.yml").read_text()
        self.assertIn("branches: [main]", workflow)
        self.assertIn("- 'AGENTS.md'", workflow)
        self.assertIn("- 'references/**'", workflow)
        self.assertIn("if: github.ref == 'refs/heads/main'", workflow)
        self.assertIn("needs: preflight", workflow)
        self.assertIn("if: needs.preflight.outputs.enabled == 'true'", workflow)
        self.assertNotIn("workflow_dispatch:", workflow)

    def test_model_evaluation_preflight_skips_without_opt_in_or_key(self):
        cases = (
            ("", "", "opt-in disabled", False),
            ("true", "", "OPENAI_API_KEY is not configured", False),
            ("true", "test-only-key", "three synthetic fixtures", True),
        )
        for opt_in, key, summary_text, should_run in cases:
            with self.subTest(opt_in=opt_in, key_configured=bool(key)):
                with tempfile.TemporaryDirectory() as directory:
                    output = Path(directory) / "output"
                    summary = Path(directory) / "summary"
                    env = {
                        **os.environ,
                        "ENABLE_SKILL_EVALS": opt_in,
                        "MODEL_API_KEY": key,
                        "GITHUB_OUTPUT": str(output),
                        "GITHUB_STEP_SUMMARY": str(summary),
                    }
                    result = subprocess.run(
                        ["bash", str(ROOT / "evaluations/preflight.sh")],
                        env=env, capture_output=True, text=True, check=True,
                    )
                    self.assertIn(summary_text, summary.read_text())
                    self.assertEqual(output.read_text() if output.exists() else "", "enabled=true\n" if should_run else "")
                    if opt_in == "true" and not key:
                        self.assertIn("::warning::", result.stdout)
                    if key:
                        self.assertNotIn(key, result.stdout)

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
