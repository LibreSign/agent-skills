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
Could we add a regression test for a missing record here? If the lookup can return null, this call may fail before the request can be handled. Please check that case and guard it if the test reproduces the failure.
```

**Human decision:** Check the proposed text and the current line before posting. No review action has been submitted.

If there are no supported findings, say “No PR comment recommended” and give a concise reason and material verification limits. If findings are clearly separate, give each its own location and copyable block. Put citations, source URLs and the reviewer's own evidence outside the block unless the comment itself needs the reference.
