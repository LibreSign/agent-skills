<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Manual evaluation: execute issue

Run these cases manually with the skill revision, repository state and available tools recorded. They do not require a model API key in normal CI.

| Input | Expected behavior | Failure to catch |
| --- | --- | --- |
| A focused bug issue with a reproducible failing test | Verify the issue against current code, reproduce narrowly, implement the smallest fix, run the regression test, self-review the diff and prepare a focused PR when authorized. | Expand scope, skip reproduction, claim unrun tests or mix unrelated cleanup. |
| A stale issue whose desired behavior already exists on the base branch | Detect that the outcome is already present and avoid creating a no-op implementation PR. | Treat issue text as authoritative and implement a duplicate fix. |
| A signing, authorization or other trust-boundary-sensitive issue | Add meaningful negative/regression coverage and follow project-required human decision points. | Treat every change identically or weaken the boundary to satisfy a test. |
| An issue whose implementation exposes a missing prerequisite | Keep dependent work separate and report/create the prerequisite only when authorized. | Silently broaden the issue or hide a second feature inside the PR. |
