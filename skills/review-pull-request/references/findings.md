<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Finding decisions

## Evidence threshold

An issue is ready for a firm comment when the review can describe the condition, the affected execution path or contract, the consequence, and why the change introduces or exposes it. Check upstream contracts and local policy before requiring a particular tool, version, browser test or coding style. For uncertain cases, ask for a focused reproduction or targeted test and say what outcome would change the recommendation. Do not turn a possibility into a stated fact.

Tests are also code to review. Inspect whether a test would fail for the wrong behavior and whether it asserts an observable result rather than coupling to incidental call counts. Mutation scores and coverage percentages are clues, not goals that justify brittle tests. End-to-end coverage should follow important user or system workflows, not mirror source filenames. A passing CI job does not prove that a missing scenario is covered; an intermittent failure must be investigated before blaming the PR.

For a complex branch, identify a concrete path that violates a requirement, hides a failure, duplicates consequential logic or makes a meaningful test impractical. Recommend a simpler design or an established project pattern only when it resolves that issue; don't impose a named design pattern or a universal cyclomatic-complexity threshold. If the project measures complexity, inspect the actual rule and result. If it uses mutation testing, inspect surviving mutants and the assertions they challenge; otherwise reason about changed conditions and boundary cases without predicting a mutation-test failure. Explain the observable consequence and a focused test, not a hypothetical tool score.

Let configured linters, formatters and static checks report routine deterministic violations. Verify that they actually run on the affected files and that required checks pass; avoid duplicating their ordinary annotations as PR comments. Investigate a check that is disabled, skipped or unable to cover the change. Security scanners likewise provide leads, not clearance: manually test relevant authorization, data flow and business logic when those paths change. Escalate a proven material risk even if a linter stays green; never disclose sensitive exploit details in a public draft.

Follow established repository conventions that affect interoperability, maintainability or a documented project standard. For a merely aesthetic preference, prefer no comment. If the PR demonstrably breaks a required check, identify the failure and its scope; don't assume that a suggested rewrite passes the linter without running it or checking its rules.

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

State the affected behavior and why it matters, then make a concrete, actionable request with an acceptable outcome. Prefer a minimal reproducible scenario over broad “add tests” language. Ask a focused question only when a project contract or relevant fact is genuinely unresolved; the author should not have to guess what improvement is requested. Offer a specific replacement sentence when reviewing misleading documentation. Use objective, respectful language and distinguish required changes from optional advice. Do not include web citations or internal reviewer analysis inside the copyable comment unless the source itself is needed for the author to act.

When the exact replacement is small, correct for the target revision and consistent with project style, consider a GitHub `suggestion` inside the copyable comment. The selected current diff line or contiguous range must exactly match the code being replaced; the suggestion contains the complete replacement, including needed indentation. Include a brief explanation before it. Do not present an unverified rewrite, multi-file change or substantial redesign as one-click replacement. A suggestion is still just a draft until the interacting human elects to post it, and applying it later changes the author's branch.
