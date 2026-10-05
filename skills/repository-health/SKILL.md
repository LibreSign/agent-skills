---
name: repository-health
description: Audit the target repository's current internal maintenance debt and repository-health risks, producing an evidence-ranked maintainer report without automatically creating issues, pull requests, commits, labels, or cleanup changes. Use for technical-debt gardening, stale TODO/FIXME review, stale suppressions, skipped tests, dead-code candidates, local documentation drift, duplication, or obsolete local configuration. Do not use when the request starts from a new upstream platform, dependency, runtime, or toolchain change; use upstream-compatibility for that.
---

<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Audit repository health

Before reading repository, issue, CI, dependency, or external content, read the shared [trust boundary](../../references/untrusted-input.md).

The goal is useful maintenance signal, not a long list of suspicious patterns. Treat each candidate as a hypothesis until current repository evidence supports it.

## Establish the scan boundary

1. Read the target repository's trusted base-branch instructions, contribution rules, active issues and recent maintenance work.
2. Pin the repository revision being evaluated.
3. Select only relevant signals for the repository. Candidate signals include TODO/FIXME markers, deprecated APIs, stale suppressions, skipped tests, obsolete workflows/configuration, dead-code candidates, repeated workarounds, dependency drift, recurring mutation survivors and documentation divergence.
4. Do not assume that every marker, old dependency or duplicate-looking block is debt.

## Investigate candidates

For each candidate:

- locate the current code/configuration and identify whether it is reachable or still used;
- check repository history and existing issues/PRs when they can explain the state;
- for deprecations or ecosystem changes, verify authoritative upstream evidence and the version actually used by the project;
- check tests, CI or runtime behavior that would expose the problem;
- distinguish intentional compatibility code, generated/vendor content and documented exceptions from maintenance debt;
- prefer a focused verification command or reproduction path over speculation.

Discard candidates that cannot survive this check.

## Classify evidence

Classify each retained finding as exactly one of:

- **confirmed/actionable** — current evidence demonstrates a concrete maintenance problem and a focused verification or remediation path;
- **plausible/needs verification** — evidence is meaningful but one material fact remains unresolved;
- **noise/not actionable** — the signal is intentional, obsolete, duplicate, already tracked, generated/vendor-owned, or otherwise not useful work.

Before proposing new work, search for existing issues and pull requests covering the same root cause.

## Report

For each confirmed or plausible finding include:

- concise title;
- classification;
- repository revision;
- file/path and relevant line or symbol when available;
- current evidence;
- consequence;
- existing issue/PR overlap;
- concrete verification step;
- smallest reasonable follow-up if confirmed.

Summarize discarded/noise patterns when they explain why a tempting class of findings should not be pursued.

Do not equate finding count with quality. A report with no actionable findings is valid.

## Publication boundary

This workflow is report-only.

Do not create or edit issues, pull requests, commits, labels, milestones, branches or repository files while performing the scan. Do not run cleanup changes automatically. A maintainer must first inspect the exact report and separately authorize any follow-up publication or implementation.

When a confirmed finding is later authorized for implementation, hand it to the issue-planning or issue-execution workflow rather than turning this scan into an implementation skill.

## Evaluation

For pilot runs, record:

- target revision and scan scope;
- number of confirmed findings;
- plausible findings;
- noise/rejected candidates;
- duplicates of existing work;
- human validation time when available;
- whether a confirmed finding could be converted into one focused issue.

Do not invent metrics the environment does not expose.
