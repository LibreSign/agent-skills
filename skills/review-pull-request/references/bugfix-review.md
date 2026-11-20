<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Reviewing reported bugs and deciding backports

Read this when a PR fixes a reported bug, particularly when its author filed the issue, or when supported release branches may need the fix. A plausible narrative and a green test suite are leads, not independent reproduction.

## Establish the contract before judging the patch

1. Read the linked issue, reproduction steps, environment/version, reported outcome and proposed explanation separately. Identify the intended user-visible outcome independently of the proposed fix. Ask whether the issue could be configuration, pre-existing behavior, already fixed upstream, or a different root cause.
2. Check the behavior on the **reported release** and the PR's **base branch** independently. Trace the actual caller, state transitions, error handling and downstream consumer. Do not silently transfer a diagnosis across changed implementations; a shared suspicious line does not establish the same bug.
3. Start with a minimal reachable case and a valid control. Prefer reproducing before the fix and verifying after it in a disposable environment. If execution is unavailable, say which part of the path is established from code and which causal link or runtime result remains unverified.
4. Check existing safeguards and tests before proposing a change: API validation, authorization, transactions, retries, asynchronous workers, stored-state predicates and cleanup. Reject candidate findings contradicted by those protections. A realistic fault-injection scenario must show where an exception or retry can actually occur, not assume an impossible state.
5. Separate evidence for the **reported original defect**, the **proposed fix's effect**, and **new regressions introduced by the patch**. A test of internal setter calls may prove a local invariant without proving the reported workflow succeeds. Do not demand an end-to-end fixture when an existing focused test already proves the behavior; add E2E coverage when it materially exercises the boundary.

## Verify retry and state correctness

For a multi-step operation, map which records and external artifacts are written, when they become visible and how retries resume. Distinguish sequential retries from overlapping requests or workers; a check on an in-memory entity is not automatically a concurrency guarantee. For a suspected partial write, trace transaction boundaries, persistence order, reload and recovery paths before labeling it a defect. Propose fault injection only when it discriminates between a safe recovery and a reachable inconsistency.

When asking for a regression, specify the setup, action, observable assertions and a control that must continue to pass. Give implementable guidance (test level, likely fixture or method, and named `#[DataProvider]` / `it.each` cases when several inputs share one contract). Prefer testing the actual state after execution over mock call counts. Keep a concise maintainer comment; do not write speculative production code into a suggestion.

## Decide release impact rather than guessing a cherry-pick list

When the user asks which stables need backports, or the defect affects supported releases:

1. Identify supported release branches from the target project's **current support policy**, not merely branch existence.
2. For each supported stable, inspect the affected implementation and relevant callers/dependencies at that stable's HEAD. Mark **verified affected**, **code path matches but runtime unverified**, **not affected**, or **requires further investigation**; record version and decisive difference.
3. Recommend backports only when the behavior is relevant to that branch, adapting code and regression tests to its APIs. Distinguish a safe cherry-pick from a semantically equivalent implementation requiring adaptation. Do not assume a fix targeting a development branch reproduces the old bug there.
4. Treat abandoned or unsupported branches separately. A matching line in an old branch is not evidence of a current maintenance commitment.

## Review handoff

Keep three decisions separate: (a) technical merit of the proposed patch and verified concerns; (b) merge gates such as first-time-contributor workflow approval, DCO and required CI; (c) optional future backport work. `action_required` or `waiting for approval` means the checks did not execute, not that code failed. Distinguish failing tests, skipped checks and unstarted jobs.

Before giving a blocking inline comment, test the counterargument and state what evidence would reverse the conclusion. An untested possibility may justify a specific verification request, but not a categorical P1 finding by default. For a first-time contributor, make the smallest clear request that can move the PR forward rather than an open-ended redesign.