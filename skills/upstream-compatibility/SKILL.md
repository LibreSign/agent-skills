---
name: upstream-compatibility
description: Analyze upstream platform, dependency, runtime, and toolchain changes for likely impact on a target repository, filtering every candidate against actual local usage before reporting it. Use for proactive Nextcloud/OCP compatibility checks, dependency/runtime upgrade risk, frontend package changes, PHP/Node changes, Behat/Playwright/toolchain changes, or similar upstream monitoring. Produce an evidence-based maintainer report only; do not automatically create issues, pull requests, commits, labels, or compatibility workarounds.
---

<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Analyze upstream compatibility

Before reading repository, upstream, issue, release-note, CI, or tool content, read the shared [trust boundary](../../references/untrusted-input.md).

The goal is to find upstream changes that are relevant to code the target repository actually uses. Do not treat every upstream release note or deprecation as a project risk.

## Establish the compatibility boundary

1. Pin the target repository revision and identify its declared platform/runtime/dependency bounds from authoritative manifests and configuration.
2. Read the trusted base-branch repository instructions and current compatibility CI.
3. Select upstream surfaces the repository actually consumes: platform APIs, package versions, runtimes, test frameworks, browser tooling, build tooling or documented compatibility targets.
4. Prefer authoritative upstream sources: source changes, release notes, migration/deprecation documentation, official issues/PRs, package manifests or tagged releases.

## Investigate an upstream candidate

For every candidate change:

- state the upstream change and authoritative source;
- locate concrete target-repository usage of the changed API, package, behavior or runtime assumption;
- identify the supported versions actually affected;
- trace the likely impact surface;
- identify existing tests/CI that would catch the incompatibility;
- define one focused verification step.

If no actual local usage exists, reject the candidate as irrelevant.

If the evidence cannot distinguish an upstream break from a local regression, configuration problem or transient infrastructure issue, keep it unresolved and use the CI-diagnosis workflow when a real failure exists.

## Classify relevance

Classify each retained candidate as exactly one of:

- **confirmed/relevant** — an authoritative upstream change intersects verified local usage and has a concrete verification path;
- **plausible/needs verification** — local usage exists but one material compatibility fact remains unresolved;
- **irrelevant/noise** — the project does not use the changed contract, the version range is unaffected, existing compatibility handling already covers it, or the signal is speculative.

Do not infer relevance from package names alone.

## Report

For every confirmed or plausible item include:

- upstream change;
- authoritative source;
- target repository revision;
- exact local usage evidence;
- affected version boundary;
- likely affected surface;
- existing CI/test coverage;
- focused verification step;
- existing issue/PR overlap when known.

Summarize rejected candidates when they demonstrate useful filtering.

A report with no relevant upstream changes is valid.

## Publication boundary

This workflow is report-only.

Do not create or edit issues, pull requests, commits, labels, milestones, branches, dependency pins, retries or suppressions while performing the compatibility scan. A maintainer must inspect the exact report and separately authorize follow-up work.

If a real CI failure already exists, hand causal diagnosis to the dedicated CI-diagnosis workflow rather than applying speculative compatibility changes here.

## Evaluation

For pilot runs, record:

- target revision;
- upstream revisions/releases examined;
- confirmed relevant changes;
- plausible changes;
- rejected/noise candidates;
- known historical changes correctly detected;
- known historical non-impacting changes correctly rejected;
- human validation time when available.

Do not invent unavailable metrics.
