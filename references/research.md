<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Sources and design choices (September 2026)

The sources below inform the workflow; their measured outcomes are not guarantees for LibreSign, another project, a future model, or a skill running with different tools. Read the target repository's current rules and live PR state during each review.

| Source | Relevant result | Implication and limit |
| --- | --- | --- |
| [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills) and [Package plugins](https://developers.openai.com/plugins/build/plugins) | A short `SKILL.md` can load task-specific references; a portable plugin can package skills without an MCP server. | Keep workflow and packaging separate from live GitHub access. |
| [OpenAI: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills) | Defines a captured run, deterministic checks and judgment rubrics; includes positive and negative triggers. | Automate narrow fixture checks; separately judge usefulness and spontaneous activation in a real installed environment. |
| [OpenAI: Codex GitHub Action](https://github.com/openai/codex-action) | Runs Codex with a constrained permission profile, optional output schema and API secret. | Run synthetic read-only evaluations only on trusted refs; never equip the evaluation job to post to a PR. |
| [REUSE Specification 3.3](https://reuse.software/spec-3.3/) and [REUSE Action](https://github.com/fsfe/reuse-action) | REUSE requires per-file licensing metadata and full texts in `LICENSES/`; its action runs `reuse lint`. | Keep `COPYING` for GitHub's license recognition; check REUSE compliance in every PR. |
| [OpenAI: Custom Code Review rules](https://developers.openai.com/blog/custom-code-review-rules-for-codex) | Scope repository invariants; evaluate violations, safe exceptions and unrelated changes; keep mechanical checks in CI. | Read the target's `AGENTS.md`; avoid broad rules that create noise. Its internal reported percentages are not a general model accuracy estimate. |
| [GitHub: About Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) | Separates repository instructions, `AGENTS.md` and task-specific skills; says to validate AI feedback with human review. | Do not replace project policy or a human publication decision. |
| [OpenStack: How to Review Changes](https://docs.openstack.org/project-team-guide/review-the-openstack-way.html) | Differentiate questions, positive feedback and blocking defects; blockers need actionable reasons. | Transfer the judgment, not Gerrit's vote mechanics. |
| [Google: What to look for](https://google.github.io/eng-practices/review/reviewer/looking-for.html) and [writing comments](https://google.github.io/eng-practices/review/reviewer/comments.html) | Look beyond the diff; ask whether tests detect bad behavior; explain severity and why a comment matters. | Valuable engineering guidance, not a binding LibreSign policy. |
| [Turzo and Bosu, Empirical Software Engineering (2023)](https://arxiv.org/abs/2302.11686) | OpenDev review usefulness relates to technical value and comprehensible, constructive language. | Do not mistake polite wording for a technically correct finding. |
| [RovoDev, ICSE SEIP (2026)](https://arxiv.org/abs/2601.01129) | Field evaluation reports that 38.7% of comments preceded code changes. | Subsequent edits are a proxy for usefulness, not proof that all comments found bugs; setting differs. |
| [c-CRAB, 2026 preprint](https://arxiv.org/abs/2603.23448) | Evaluated agents collectively solved about 40% of its human-review-derived tasks; AI and human reviewers noticed different aspects. | Human comments are incomplete ground truth; no single-agent score carries over here. |
| [SWE-PRBench, 2026 preprint](https://arxiv.org/abs/2603.26130) and [CR-Bench, 2026 preprint](https://arxiv.org/abs/2603.11078) | Report missed human-flagged issues in a diff-only setting and the trade-off between recall and spurious findings. | Measure both omissions and noisy findings locally; avoid claims that a clean result proves safety. |
| [Anthropic: Code Review Plugin](https://github.com/anthropics/claude-code/tree/main/plugins/code-review) | Separates local report from optional posting and considers PR history. | Preserve the useful separation without copying its numeric confidence cutoff or assuming parallel agents improve accuracy. |

The research on current model ability will age. Prefer a small, repeatable local evaluation with recorded model, revision and context over a timeless assertion of superiority or inadequacy. Security findings require the target project's private reporting route.
