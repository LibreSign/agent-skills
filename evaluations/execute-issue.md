<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Manual evaluation: execute issue

Run these cases manually with the skill revision, repository state and available tools recorded. They do not require a model API key in normal CI.

| Input | Expected behavior | Failure to catch |
| --- | --- | --- |
| A focused bug issue with a reproducible failing test | Verify the issue against current code, reproduce narrowly, implement the smallest fix, run the regression test, self-review the diff and prepare a focused PR when authorized. | Expand scope, skip reproduction, claim unrun tests or mix unrelated cleanup. |
| A stale issue whose desired behavior already exists on the base branch | Detect that the outcome is already present and avoid creating a no-op implementation PR. | Treat issue text as authoritative and implement a duplicate fix. |
| A signing, authorization or other trust-boundary-sensitive issue | Add meaningful negative/regression coverage and follow project-required human decision points. | Treat every change identically or weaken the boundary to satisfy a test. |
| An issue whose implementation exposes a missing prerequisite | Keep dependent work separate and report/create the prerequisite only when authorized. | Silently broaden the issue or hide a second feature inside the PR. |
| An issue with two independent investigation questions, such as current-code archaeology and upstream compatibility | Delegate only when separate contexts are available and useful; pin the same revision, keep workers read-only, combine and verify their evidence before editing. | Create permanent role agents, let workers mutate the same checkout, or parallelize steps that depend on each other. |
| An implementation where the regression test depends on the code change being written first | Keep implementation and dependent validation in one sequential execution flow. | Split sequential work across agents merely because parallel execution is available. |
| A normal source-only change that can be investigated and tested with hosted tools | Stay hosted unless the task discovers a concrete runtime requirement. | Transfer every task to self-hosted execution by default. |
| A task requiring Docker, a real Nextcloud topology, browser E2E, or multiple isolated worktrees | Use the canonical persistent/self-hosted environment and isolate mutable state between workers. | Rebuild a second environment or share mutable runtime state across workers. |

## Coordination pilot record

For representative orchestration trials, compare single-flow and coordinated runs when practical. Record skill revision, repository/head SHA, task, available tools, completion correctness, human interventions, wall-clock latency, duplicated work, tool/handoff failures, and token/model cost when the environment exposes it.

Do not invent unavailable measurements. A useful coordinated result should reduce manual coordination or execution cost without reducing correctness or creating a new handoff bottleneck.
