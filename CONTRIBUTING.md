<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Contributing

Submit changes through a PR. Keep each `SKILL.md` short and use linked references for detail. The target repository supplies its own coding rules; this plugin should remain useful across projects. Do not commit private chat history, credentials, private PR content, or unpublished vulnerability details. Treat PR descriptions, source comments and issue bodies as untrusted data.

## Run the required checks

Run `python3 -m unittest discover -s tests -v` and `reuse lint` locally. The GitHub Actions workflow runs both on pull requests and pushes to `main`. `LICENSE` contains the full text at the project root; REUSE requires the corresponding text in `LICENSES/AGPL-3.0-or-later.txt`. Give new files SPDX copyright and license metadata, or add a narrowly scoped entry to `REUSE.toml` for formats without comments. Do not add a generic catch-all annotation that conceals unlicensed files.

These checks catch broken package paths, invalid metadata, missing license information, a missing link to the [shared trust boundary](references/untrusted-input.md), and accidental removal of the human authorization rule. They do not establish that a finding is accurate, that a line anchor matches a live PR, that the model obeys the trust boundary, or that the plugin triggers in a particular ChatGPT environment.

## Evaluate behavior

The optional model evaluation runs on pushes to `main` that change a skill, shared reference, repository instructions, fixture or the workflow. It has no manual branch dispatch. It is off by default: without `ENABLE_SKILL_EVALS=true`, preflight prints a notice and skips the model. If enabled but the `OPENAI_API_KEY` secret is missing, preflight prints a warning and skips the model without failing the workflow. Neither case sends API requests. Only when both are present does the action evaluate three local synthetic fixtures, which consumes API usage. The action has a read-only permission profile, produces no PR comment and fails if its machine-checkable expectations are broken. A workflow from an unreviewed PR does not receive this secret. Review the traces and candidate text yourself; the automatic grader is intentionally narrower than the review task.

For changes to instructions, compare at least one expected defect, one clean control and one case that tries to persuade the reviewer to publish. Exercise attacks in PR discussion, commit messages, source and logs, and in an instruction file changed by the PR; check both whether the agent performed any unauthorized tool action and whether it changed its findings. Run these in an isolated environment without real write credentials. Also exercise a fresh PR in a real project before treating the skill as mature. Log the model, skill revision, PR head, available tools, executed checks, accurate and spurious findings, line accuracy and human validation time. Historical comments in [`evaluations/review-pull-request.md`](evaluations/review-pull-request.md) are candidates, not a complete answer key. Update the fixtures when a real miss shows a generalizable failure; avoid scoring only literal phrases from the skill.
