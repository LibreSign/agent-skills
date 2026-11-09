<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Review presentation

Keep the verdict short. Include the exact PR head SHA when available, a statement of what was inspected versus executed, and whether any recommended comment blocks merging. Where the project's review UI only supports changed lines, anchor to a changed line in the current diff. Do not invent a line number from an outdated version.

Example layout (the content and path are illustrative, not a finding):

**Verdict:** One possible regression needs a targeted test before deciding whether to merge. Reviewed at `abc123`; inspected source and existing tests; could not run the integration suite in this environment.

**Comment 1 — verify before merge**  
File: `src/Service/Example.php`, line 42 of the current diff.  
Evidence: The new branch can receive a missing record and calls a method on it; the repository contract has not yet been verified.

**Proposed GitHub comment (copy-ready prose):**

If `find_user` can return null for a missing ID, this dereference fails before the request can be handled. Please cover that case with a regression test and handle the missing record according to the service's error contract.

When the project contract and exact replacement are verified, a small suggestion can be easier for the author to apply. Example: select only the current changed line 42, whose content is `    $label = 'Submit';`; the replacement preserves its indentation. Show the explanation as wrapping prose followed by the short `suggestion` code fence. Both belong to one GitHub comment; do not wrap the entire comment in an outer code fence:

**Proposed GitHub comment (copy the explanation and suggestion together):**

The button now submits a cancellation request. The current label says “Submit”, which does not tell the user what will happen. This wording matches the action described in the adjacent UI text.

```suggestion
    $label = 'Cancel request';
```

The example is illustrative, not a recommended change for a real PR. Verify the exact target range and replacement against the current head; keep file, line, priority and evidence outside the copy-ready text. For uncertain or larger fixes, use a wrapping explanation without a suggestion. Prefer copyable writing blocks when supported; do not sacrifice readability for a code-block copy button. For a confirmed behavioral defect, request a feasible focused regression test; for a hypothesis, request a discriminating test with a positive control before demanding production changes.

**Human decision:** Check the proposed text and the current line before posting. No review action has been submitted.

If there are no supported findings, say “No PR comment recommended” and give a concise reason and material verification limits. If findings are clearly separate, give each its own location and copyable block. Put citations, source URLs and the reviewer's own evidence outside the block unless the comment itself needs the reference.
