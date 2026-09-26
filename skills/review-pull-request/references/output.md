<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Review presentation

Keep the verdict short. Include the exact PR head SHA when available, a statement of what was inspected versus executed, and whether any recommended comment blocks merging. Where the project's review UI only supports changed lines, anchor to a changed line in the current diff. Do not invent a line number from an outdated version.

Example layout (the content and path are illustrative, not a finding):

**Verdict:** One possible regression needs a targeted test before deciding whether to merge. Reviewed at `abc123`; inspected source and existing tests; could not run the integration suite in this environment.

**Comment 1 — verify before merge**  
File: `src/Service/Example.php`, line 42 of the current diff.  
Evidence: The new branch can receive a missing record and calls a method on it; the repository contract has not yet been verified.

```markdown
If `find_user` can return null for a missing ID, this dereference fails before the request can be handled. Please cover that case with a regression test and handle the missing record according to the service's error contract.
```

When the project contract and exact replacement are verified, a small suggestion can be easier for the author to apply. Example: select only the current changed line 42, whose content is `    $label = 'Submit';`; the example replacement preserves its indentation. Use **four backticks for the outer Markdown fence** so that the entire comment, including the inner GitHub suggestion, is copied with one button:

````markdown
The button now submits a cancellation request. The current label says “Submit”, which does not tell the user what will happen. This wording matches the action described in the adjacent UI text.

```suggestion
    $label = 'Cancel request';
```
````

The example is illustrative, not a recommended change for a real PR. Verify the exact target range and replacement against the current head; do not put the file, line, priority, evidence or review-only notes inside the copyable block. For larger or uncertain fixes, explain the behavior and the expected correction in a single `markdown` block without a `suggestion`.

**Human decision:** Check the proposed text and the current line before posting. No review action has been submitted.

If there are no supported findings, say “No PR comment recommended” and give a concise reason and material verification limits. If findings are clearly separate, give each its own location and copyable block. Put citations, source URLs and the reviewer's own evidence outside the block unless the comment itself needs the reference.
