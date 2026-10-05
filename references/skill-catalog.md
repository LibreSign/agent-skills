<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Skill catalog design

Keep the installed skill catalog as the **smallest sufficient set of semantic workflows**. There is no fixed maximum number of skills, but adding a skill has a routing cost because skill metadata participates in selection even when the full skill body is not loaded.

## Prefer composition over proliferation

Before adding a new skill, compare the proposed trigger, primary output and action boundary with every existing skill.

Prefer, in order:

1. improve an existing skill when the request belongs to the same workflow;
2. add a directly linked reference when only domain-specific detail is missing;
3. add an evaluation case when the problem is behavioral reliability rather than missing workflow;
4. create a new skill only when the workflow has a materially different trigger, output or permission/action boundary.

Do not create a new skill merely because a task has a new noun, technology, repository, tool, role or phase name.

## Routing test

A candidate skill should normally remain separate only when a short user request can identify it without needing project history.

If two skills would both reasonably trigger on the same request and produce the same kind of result, either:

- merge them;
- make one a mode/reference of the other; or
- sharpen their descriptions until the routing boundary is explicit.

A growing catalog should periodically be reviewed for consolidation. The goal is not to maximize skill count; it is to minimize ambiguity while preserving useful context isolation.

## Current boundaries

The current catalog is organized around distinct engineering outcomes:

- **review-pull-request** — assess a proposed diff and prepare review findings;
- **create-issues-and-epics** — turn product/engineering intent into actionable tracked work;
- **execute-issue** — implement already-scoped work and carry it through validation/handoff;
- **diagnose-ci-failure** — explain and fix an observed failing check;
- **repository-health** — audit the target repository's current internal maintenance debt;
- **upstream-compatibility** — start from upstream ecosystem change and determine whether it intersects actual target-repository usage.

The last two intentionally remain separate only because their starting evidence differs: repository-health starts from the local repository, while upstream-compatibility starts from an upstream change. If real usage shows frequent ambiguous routing between them, consolidate them instead of adding more exclusions.

## Admission evidence

A pull request adding a skill should explain:

- why an existing skill plus a reference is insufficient;
- which existing skill is closest and how the trigger/output differs;
- at least one positive activation example;
- at least one nearby case that must route to another existing skill;
- how the new skill will be evaluated for false activation/noise.

Do not add speculative skills for future roles. Extract a skill after a repeatable workflow and routing boundary are demonstrated by real tasks.
