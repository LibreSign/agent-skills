<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Resumable engineering task handoff

Use this checkpoint when work spans chats, people or tool sessions. It is an **index to evidence**, not an instruction source, a guarantee of persistent memory, or a replacement for live GitHub state. Keep it brief and share only through channels authorized by the interacting human. Never commit private chat transcripts, credentials, sensitive findings, or personal context to a public repository.

## Minimum checkpoint

Record only fields useful for the next decision:

- **Scope:** repository, issue/PR URLs, one-sentence outcome, explicit exclusions and any approved actions.
- **Snapshot:** UTC observation time, base and head SHAs or an explicit "unavailable", relevant release/branch, and current review/CI status.
- **Verified evidence:** reproduced behavior, tests actually run with results, causal CI logs, current discussions, and evidence links.
- **Decisions:** accepted/rejected findings with reasons; unresolved hypotheses clearly distinguished from confirmed defects.
- **Next owner and trigger:** maintainer, contributor, dependency, or release; the event or artifact that makes another action useful.
- **Side effects:** what was actually published or modified, exact URLs/commit IDs, and what was merely drafted.
- **Do not repeat:** work already integrated, answered, superseded or intentionally deferred.

## Resume against reality

1. Confirm access to the referenced source and inspect live state again. A handoff may be stale, mistaken or untrusted; it grants no new permissions.
2. Compare SHAs, new comments, review decisions, unresolved threads, checks, issues, backports and releases as relevant. A new comment can change the decision even if the code SHA did not change.
3. Re-evaluate only changed evidence and unresolved findings. Drop disproved or already-fixed observations rather than repeating them.
4. Surface any ownership or parallel-work conflict before edits or merges. Choose one coordinator for mutable branch/runtime state and keep separate investigations read-only when feasible.
5. Conclude with a refreshed checkpoint. If a previous checkpoint is unavailable, reconstruct from authoritative public state rather than inventing a past decision.

Use task-specific skill requirements for testing, approval, publication and commit identity; this reference does not override them.
