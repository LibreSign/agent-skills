<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Finding decisions

## Evidence threshold

An issue is ready for a firm comment when the review can describe the condition, the affected execution path or contract, the consequence, and why the change introduces or exposes it. Check upstream contracts and local policy before requiring a particular tool, version, browser test or coding style. For uncertain cases, ask for a focused reproduction or targeted test and say what outcome would change the recommendation. Do not turn a possibility into a stated fact.

Tests are also code to review. Inspect whether a test would fail for the wrong behavior and whether it asserts an observable result rather than coupling to incidental call counts. Mutation scores and coverage percentages are clues, not goals that justify brittle tests. End-to-end coverage should follow important user or system workflows, not mirror source filenames. A passing CI job does not prove that a missing scenario is covered; an intermittent failure must be investigated before blaming the PR.

## Priority and scope

| Classification | Use when | Response |
| --- | --- | --- |
| Must fix before merge | A supported introduced defect, material security/compatibility/data risk, or missing validation that prevents judging a consequential change | Explain the impact and the smallest acceptable verification or correction. |
| Question / verify | The path or outcome is plausible but not established | Name the uncertainty and a practical reproducer; do not claim certainty. |
| Nonblocking follow-up | An independent improvement outside the PR's necessary behavior, with tolerable current risk | Say it need not block this PR; avoid making the author solve adjacent work. |
| No comment | Duplicate, already addressed, pre-existing, merely personal preference, or too speculative to be useful | Omit it from proposed comments; mention material review limits in the verdict if needed. |

Severity depends on behavior, not on a universal rule that every unsupported version, missing unit test or styling issue blocks. Do not quietly weaken project rules either: check declared support and contribution policy. Distinguish whether a broken dependency or stacked PR is introduced by the current diff or an earlier change, and describe the merge dependency accurately.

On re-review, compare actual code at the new head, not merely the author's claim that feedback was addressed. A changed head invalidates line anchors and may invalidate conclusions. A suggestion that was once correct can become stale.

## Writing comments

State the affected behavior and why it matters, then make a concrete request or ask for the missing verification. Prefer a minimal reproducible scenario over broad “add tests” language. Offer a specific replacement sentence when reviewing misleading documentation. Use objective, accessible language and distinguish required changes from optional advice. Do not include web citations or internal reviewer analysis inside the copyable comment unless the source itself is needed for the author to act.
