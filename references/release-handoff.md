<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Release handoff for contributor fixes

Read this reference only when determining whether a merged fix is available to users, or when triage exposes pending publication.

Use the target project's documented release engine and version policy as the source of truth. Do not implement a second release planner inside these skills. In repositories using LibreCodeCoop/release-tool, read its current lifecycle and troubleshooting documentation and verify its authoritative preflight/plan instead of inferring readiness from GitHub PR titles.

Distinguish the following states with evidence and links:

1. **Merged:** the required code commit is in the correct branch; verify which supported branches contain it and any open backports.
2. **Prepared:** a release plan and preparation PR exist for a pinned planning base. A draft PR or one green DCO check is not an approved release.
3. **Finalized:** the project's release engine successfully performed finalization, required branch synchronization and artifact validation on the intended commit.
4. **Published:** the release is actually published in the intended distribution channel, with the required artifact/signing result verified. Public indexes may lag; do not replace the publisher signal with a cached listing.
5. **Reporter informed:** the user has received a correct version or availability statement, distinct from closing an issue.

A stale plan is not repaired by manually modifying generated preparation metadata. Re-run the canonical planning process only when authorized, and present any human merge/publication gates separately. Report unresolved checks, supported-version limits and who owns the next step.

This reference is read-only guidance; it does not authorize creating releases, modifying branches, publishing artifacts, closing issues, or changing repository permissions.
