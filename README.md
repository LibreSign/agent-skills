<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# LibreSign agent skills

Reusable skills for LibreSign and other free software projects. Each skill guides a task and prepares results for a human to review.

## Skills

| Skill | What it does |
| --- | --- |
| [Review a pull request](skills/review-pull-request/SKILL.md) | Investigates changes, tests and risks; prepares file and line-specific comments for a human to review. It does not publish a review or modify the PR on its own. |

## Get started

Add this repository as a marketplace with `codex plugin marketplace add LibreSign/agent-skills` and install **LibreSign Agent Skills** in ChatGPT or Codex. Select the skill, then provide a PR link or diff. Repository access depends on the tools connected to your environment.

To contribute a skill or adapt a workflow to another project, see [CONTRIBUTING.md](CONTRIBUTING.md).
