<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Activity collection and triage evidence

## Collect complete timelines

- Enumerate accessible repositories and retain explicit exclusions. Set an absolute date boundary and record when the scan ran.
- Use paginated issue/PR lists or search for candidate discovery, but collect issue comments, PR conversation comments, inline review comments and review submissions from their actual timelines. Search results and `updated_at` alone do not establish that a new comment exists.
- Some review threads are unresolved even when an author replies elsewhere; inspect the current review decision and thread resolution status before calling a PR ready.
- For long-running repos, use an incremental watermark with a small overlap, deduplicate by stable comment/review IDs, and re-read relevant older context. Do not silently stop at the API's first 100 items or GitHub Search's result limit.
- Pin the current head SHA when reporting a PR correction. Compare with the previously reviewed SHA, then check current CI and reviews; an older green run does not validate a new head.
- Cross-check comments against linked PRs, merges, releases and documented blockers. A merged backport is not a published release, and a reviewer comment need not require a new public issue response.
- Keep inaccessible/private repositories, pagination errors, rate-limit failures and incomplete windows visible as coverage limitations.

## Interpret authors and pending decisions

`OWNER`, `MEMBER` and `COLLABORATOR` describe GitHub relationships, not an employment contract. A `CONTRIBUTOR` may also belong to the company. Use verified organization membership when available; do not expose inaccessible membership information, and classify uncertain cases explicitly. Exclude known bot accounts from human wait-time prioritization; where a response declares itself AI-generated rather than personally verified, do not treat it as a contributor's firm delivery commitment.

Determine whether a maintainer still owes a decision by following the whole exchange, not merely looking for a later maintainer timestamp. Examples:

| Signal | Appropriate interpretation |
| --- | --- |
| External question, later maintainer guidance, no further change | Await contributor; do not post the same guidance again |
| External correction pushed after `CHANGES_REQUESTED` | Re-review the changed head; green checks alone do not clear review state |
| New PR linked to an issue | Follow the PR before calling the original issue abandoned |
| Closed bug fixed in branches but no release | Treat publication and user communication separately |
| External automated response disclaims human verification | No confirmed commitment; keep underlying dependency visible |
| Previous audit identified an item now merged, reviewed or answered | Reconcile as progressed; do not restart as an untouched request |

When recommending work in parallel, name ownership and potential shared-file, branch, or mutable-runtime conflicts. Keep workstations, secrets and unrelated project chats outside public handoffs.

## Report restraint

Every proposed reply must identify its recipient's actual unresolved question, not offer generic appreciation. If no actionable external activity is found, say so and state the coverage limit. Avoid a numerical "unanswered" count unless the classification criteria and sampled timelines support it.
