# SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "evaluations/orchestration_pilot.py"


def load_runner():
    spec = importlib.util.spec_from_file_location("orchestration_pilot", RUNNER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class OrchestrationPilotTests(unittest.TestCase):
    def test_single_and_coordinated_requests_share_task_and_model(self):
        runner = load_runner()
        single = runner.session_kwargs("model-x", "same task", False, 2)
        coordinated = runner.session_kwargs("model-x", "same task", True, 2)

        self.assertEqual(single["input"], coordinated["input"])
        self.assertEqual(single["agent"]["model"], coordinated["agent"]["model"])
        self.assertNotIn("multi_agent", single["agent"])
        self.assertEqual(
            coordinated["agent"]["multi_agent"],
            {"enabled": True, "max_concurrent_subagents": 2},
        )
        self.assertEqual(single["environment"], {"type": "none"})
        self.assertEqual(coordinated["environment"], {"type": "none"})


if __name__ == "__main__":
    unittest.main()
