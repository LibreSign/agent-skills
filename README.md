<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# LibreSign agent skills

Reusable, human-reviewed workflows for software projects maintained by LibreSign and other free software communities. The first skill helps investigate a pull request and prepare a review. It does not publish comments or change the pull request during a review.

## Review a pull request

Use `skills/review-pull-request/SKILL.md` with a PR URL, a diff, or a local checkout. The skill reads the affected code, repository guidance, tests, CI and relevant history, then returns a concise verdict and only the findings that survive verification. Each proposed inline comment includes a current file and line range and a separate, copyable Markdown block. A human decides whether to post it.

The skill works across repositories. The target repository's `AGENTS.md`, contribution guide, security policy, code and tests remain the authority for project-specific behavior. Guidance in this repository must not duplicate facts likely to drift with another codebase.

The first evaluation set is in [`evaluations/review-pull-request.md`](evaluations/review-pull-request.md). It records review decisions from public PRs as examples to challenge, not a complete list of true defects. See [`references/research.md`](references/research.md) for the evidence and its limits.

## Use in ChatGPT and Codex

This repository's root is an Agent Plugins package (`plugin.json`) containing one portable Agent Skill. In ChatGPT desktop or Codex, add this Git repository as a plugin marketplace with `codex plugin marketplace add LibreSign/agent-skills`, restart the app, and install **LibreSign Agent Skills** from the LibreSign marketplace. The repo catalog at `.agents/plugins/marketplace.json` points to the plugin at the repository root. Start a new chat and select the installed plugin with `@`. Alternatively, read the skill directly in a compatible local agent. Installation and connection to GitHub are separate: the skill does not grant repository access or write permissions. If a PR cannot be read, supply the diff and relevant files; the review must state the resulting limits. Workspace-wide or public-directory publication requires a separate process.

The first version deliberately includes no MCP server, app mapping, hooks, bot, or automatic GitHub workflow. Adding GitHub access later must preserve the default review-only behavior and keep any posting action separate and subject to review of the exact draft.

## Validation

Every PR runs structural checks and `reuse lint`. The opt-in model evaluation runs against synthetic fixtures on a trusted branch when a maintainer enables it and configures an API key. The CI contract and its limitations are documented in [`CONTRIBUTING.md`](CONTRIBUTING.md).
