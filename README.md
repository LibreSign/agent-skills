<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# LibreSign agent skills

Reusable skills for LibreSign and other free software projects. Each skill guides a task while preserving the target project's contribution and authorization boundaries. The catalog is intentionally bounded by semantic need rather than a numeric target: new workflows should extend or compose existing skills whenever that avoids overlapping activation.

## Skills

| Skill | What it does |
| --- | --- |
| [Handle security advisory](skills/handle-security-advisory/SKILL.md) | Coordinates confidential GHSA triage, private-fork corrections, verified releases, disclosure approval and CVE follow-up. |
| [Maintainer inbox](skills/maintainer-inbox/SKILL.md) | Triage contributor comments and PR follow-ups across repositories; reconcile prior work and prepare a verified read-only action queue. |
| [Review a pull request](skills/review-pull-request/SKILL.md) | Investigates changes, tests and risks; prepares file and line-specific comments for a human to review. It does not publish a review or modify the PR on its own. |
| [Create issues and epics](skills/create-issues-and-epics/SKILL.md) | Checks current work, drafts actionable issues and epics, and plans genuine parent and blocking links for human review before publication. |
| [Execute an issue](skills/execute-issue/SKILL.md) | Takes already-scoped work through investigation, focused implementation, validation, self-review and pull-request handoff; it may coordinate temporary independent subagents when that reduces work. |
| [Diagnose a CI failure](skills/diagnose-ci-failure/SKILL.md) | Finds the causal CI failure, distinguishes regressions from upstream/environment problems and proves a focused fix with evidence. |
| [Audit repository health](skills/repository-health/SKILL.md) | Finds actionable maintenance debt, separates signal from noise, checks duplicate work and produces a report for maintainer review without publishing changes. |
| [Analyze upstream compatibility](skills/upstream-compatibility/SKILL.md) | Filters upstream platform, dependency and toolchain changes against actual project usage and produces a focused compatibility report. |

## Install and update from one source

**Canonical distribution:** this repository is one Git-backed plugin, **LibreSign Agent Skills**, with multiple skills and shared files in `references/`. Install the complete plugin through its marketplace, not separate copies of individual skills. **Do not install a standalone `skill.zip`** for one of these skills alongside the plugin: some skills link to shared files outside their own directories, so a single-skill export is incomplete without bundling shared references. A ZIP uploaded to ChatGPT is a separate, manually maintained snapshot; it does not track Git changes.

In Codex or a supported ChatGPT desktop environment, register the repository marketplace and refresh its source with:

```sh
codex plugin marketplace add LibreSign/agent-skills
codex plugin marketplace list
codex plugin marketplace upgrade
```

For Claude Code, run `/plugin marketplace add LibreSign/agent-skills` followed by `/plugin install libresign-agent-skills@libresign-agent-skills`. Install the complete repository plugin so that shared `references/` remain accessible. The Claude manifests intentionally omit `version`, so installations can follow repository updates rather than a pinned plugin version. Verify updates in the installed client.

Install **LibreSign Agent Skills** from that marketplace in the client's Plugins Directory. `marketplace upgrade` refreshes marketplace sources; **it does not guarantee that an already installed cached plugin is refreshed or that ChatGPT web receives the same installation**. Refresh or reinstall the installed plugin through the supported client interface if needed, restart the session, and verify the installed `plugin.json` version and access to the expected skills and their shared references. The installed copy can lag the Git repository even after a merge.

**Migrating from a ZIP upload:** first confirm that the *complete* Git-backed plugin works in the same client. Only then remove the separately uploaded `handle-security-advisory` skill from **Plugins → Skills → Installed**, using the actions available in that client. Do not remove the Git-backed plugin or delete a standalone skill when it is the only accessible installation; arrange a supported plugin installation first. If a standalone distribution is genuinely required, it must be separately designed, fully self-contained, validated, versioned, and maintained as a different delivery channel.

Select a skill and provide a PR link, diff, issue context, failing workflow, repository-health question, or upstream compatibility question. Repository access depends on the tools connected to your environment.

The interface shows three representative starter prompts; every workflow in the table remains available. Other examples include "Re-review this pull request after the latest changes", "Draft issues and an epic with dependencies", "Diagnose a failing CI run", "Audit repository maintenance debt", and "Check upstream compatibility".

To contribute a skill or adapt a workflow to another project, see [CONTRIBUTING.md](CONTRIBUTING.md) and the [skill catalog design](references/skill-catalog.md).
