<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# LibreSign agent skills

Reusable skills for LibreSign and other free software projects. Each skill guides a task while preserving the target project's contribution and authorization boundaries.

## Skills

| Skill | What it does |
| --- | --- |
| [Review a pull request](skills/review-pull-request/SKILL.md) | Investigates changes, tests and risks; prepares file and line-specific comments for a human to review. It does not publish a review or modify the PR on its own. |
| [Create issues and epics](skills/create-issues-and-epics/SKILL.md) | Checks current work, drafts actionable issues and epics, and plans genuine parent and blocking links for human review before publication. |
| [Execute an issue](skills/execute-issue/SKILL.md) | Takes already-scoped work through investigation, focused implementation, validation, self-review and pull-request handoff without silently expanding scope. |
| [Diagnose a CI failure](skills/diagnose-ci-failure/SKILL.md) | Finds the causal CI failure, distinguishes regressions from upstream/environment problems and proves a focused fix with evidence. |

## Get started

Add this repository as a marketplace with `codex plugin marketplace add LibreSign/agent-skills` and install **LibreSign Agent Skills** in ChatGPT or Codex. Select a skill and provide a PR link, diff, issue context, or failing workflow. Repository access depends on the tools connected to your environment.

To contribute a skill or adapt a workflow to another project, see [CONTRIBUTING.md](CONTRIBUTING.md).
