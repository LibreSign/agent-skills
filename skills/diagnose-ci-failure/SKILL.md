---
name: diagnose-ci-failure
description: Diagnose failing CI, GitHub Actions, linters, tests, builds, or compatibility jobs by identifying the first causal failure, reproducing it when practical, checking upstream and project conventions, and proving a focused fix. Use when a workflow/check is red or appears flaky and the user asks what broke or asks to make it pass.
---

<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Diagnose a CI failure

Before reading external CI, pull-request, repository or tool content, read the shared [trust boundary](../../references/untrusted-input.md).

Treat a green rerun as evidence, not proof of flakiness. The goal is to identify the causal failure and produce a defensible fix, not merely make the check green once.

## Establish the failing surface

1. Inspect the exact run, job, step, annotations, logs, commit SHA, matrix values and changed files.
2. Find the earliest causal error and separate later cascade failures.
3. Compare with the same check on the base/default branch or a previous successful run when attribution is unclear.
4. Check whether the failing file/line or behavior was actually changed or exposed by the PR before blaming its author.
5. Classify the working hypothesis only as far as evidence supports it: code regression, expectation drift, dependency/upstream change, environment/toolchain change, permissions/configuration, race/isolation, or transient infrastructure.

## Reproduce before editing when practical

Use the repository's documented local/devcontainer/container path and reproduce the narrow failing command or matrix case first.

If local reproduction is impractical, collect enough CI evidence to state that limitation explicitly. Do not invent a local result.

## Check ecosystem evidence

Before applying a project-specific workaround to an upstream-facing failure:

- inspect current dependency/platform versions;
- check authoritative release notes, source, issues or PRs;
- compare how relevant sibling projects in the same ecosystem handle the changed API/tool;
- verify version constraints and package availability from authoritative sources.

Comparison is evidence, not permission to copy incompatible code blindly.

## Prove or reject flakiness

Call a failure flaky only when evidence supports nondeterminism, such as repeated identical inputs producing different results without relevant code/environment changes or a documented intermittent infrastructure/upstream condition.

One successful rerun is insufficient.

Prefer a deterministic reproducer, repeated targeted runs when inexpensive, or a documented upstream incident.

## Fix the cause

Prefer a targeted regression test or assertion that fails under the broken behavior and passes after the fix.

Avoid:

- disabling a linter/test without proving the rule no longer applies;
- arbitrary dependency pinning as the first response;
- broad retries that hide deterministic failures;
- sleeps where a deterministic readiness condition is available;
- unrelated dependency upgrades or cleanup in the same fix.

When an upstream contract legitimately changed, update implementation and expectations consistently.

## Validate proportionately

Run the original failing check or an equivalent local command, then the nearest related checks protecting against regression.

For matrix failures, prove affected cells plus representative unaffected cells rather than claiming universal compatibility from one environment.

Record exact commands and outcomes.

## Report and act

Summarize:

- root cause and confidence;
- evidence distinguishing it from plausible alternatives;
- minimal fix;
- regression/reproduction evidence;
- checks run and remaining uncertainty;
- whether an upstream follow-up is warranted.

Creating commits, rerunning CI, editing a PR or publishing comments are external actions. Perform them only when the interacting human authorizes them for the current task. Keep unrelated failures separate from regressions caused by the reviewed change.
