<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Release handoff for contributor fixes

Read this reference only when determining whether a merged fix is available to users, or when triage exposes pending publication.

Use the target project's documented release engine and version policy as the source of truth. Do not implement a second release planner inside these skills. In repositories using LibreCodeCoop/release-tool, read its current lifecycle and troubleshooting documentation and verify its authoritative preflight/plan instead of inferring readiness from GitHub PR titles.

Distinguish the following states with evidence and links:

1. **Merged:** the required code commit is in the correct branch; verify which supported branches contain it and any open backports.
2. **Prepared:** a release plan and preparation PR exist for a pinned planning base. A draft PR or one green DCO check is not an approved release.
3. **Finalized:** after the preparation PR is reviewed and merged, the release engine revalidates the merged state, records the exact released commit, updates milestones and initiates the configured changelog-synchronization PRs. This does not validate or publish the package.
4. **Published and verified:** after a maintainer publishes the release draft, verify the configured publisher workflow succeeded and the expected release artifact exists. Package building, signing and distribution checks belong here, not to finalization. Public indexes may lag; a published GitHub Release alone does not prove availability in another distribution channel.
5. **Reporter informed:** communicate the verified status independently of publication. Before a release, identify integrated branches without claiming an installable fix; after publication is verified, identify the published version. Closing an issue is a separate decision.

For embargoed vulnerability corrections, verify all intended supported branches and installable fixed versions before proposing public disclosure. Code merge or a GitHub release draft alone must not trigger advisory publication. Security advisory edits, CVE requests and public publication require independent human authorization; use `handle-security-advisory` for that disclosure decision.

A stale plan is not repaired by manually modifying generated preparation metadata. Re-run the canonical planning process only when authorized, and present any human merge/publication gates separately. Report unresolved checks, supported-version limits and who owns the next step.

This reference is read-only guidance; it does not authorize creating releases, modifying branches, publishing artifacts, closing issues, or changing repository permissions.
