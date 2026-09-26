<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Draft format

Show a small set of issues, each with a provisional ID, title, repository, verified type/labels/milestone and applicable project fields or “to confirm”, followed by a separate `markdown` block containing only the body that the human may paste. Keep analysis, citations, milestone capacity assumptions and authorization status outside the block. Adapt headings to the project's actual issue template. Explain which issues can be implemented in parallel and what is required to call each issue and the epic done.

Example for a fictional repository (the identifiers are provisional, not GitHub issue numbers):

**A — Epic: Make request expiration predictable**  
Repository: `example/project` · Type: to confirm · Labels: to confirm · Milestone: to confirm · Project fields: to confirm

```markdown
## Goal

Make the effective expiration of a request predictable to users and administrators.

## Origin

The behavior was reported in the linked user report; verify the current policy contract before publishing this issue.

## Done when

- [ ] The effective expiration is defined at the appropriate lifecycle point.
- [ ] Users see a message consistent with that behavior.
- [ ] The child issues' agreed outcomes have been verified.
```

**B — Persist effective request expiration**  
Repository: `example/project` · Type: to confirm · Labels: to confirm · Milestone: to confirm · Project fields: to confirm

```markdown
## Goal

Persist the server-resolved expiration for a new request so later policy changes do not silently alter it.

## Acceptance criteria

- [ ] A request created with a valid expiration retains its effective value after a policy change.
- [ ] A requester cannot choose a value prohibited by server policy.
- [ ] Tests cover an allowed override and a rejected override.

## Out of scope

Changing certificate lifetime.
```

| Child | Parent | Blocked by | Reason |
| --- | --- | --- | --- |
| B | A | None established | B is part of the epic; the example does not establish any prerequisite. |

Before publication, resolve provisional references and metadata using the project's live conventions, or identify genuinely undecided values to the human. Do not assign an invented milestone or field option. After authorization, create/link the issues in dependency order and verify native GitHub relationships and metadata; report unavailable operations rather than claiming they succeeded.

For a suitable LibreSign newcomer issue, inspect the current issue template and recent examples before adding a concise `## Good first issue` paragraph: name the existing component or contract to follow, a starting point, and the boundary that keeps the change reviewable. Where the current LibreSign convention includes `### Additional context`, retain its invitation for questions and verified community links. Do not paste that footer into issues for another project, or treat the section itself as proof that an issue deserves the label.
