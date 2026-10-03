<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Manual evaluation: diagnose CI failure

Run these cases manually with the skill revision, repository state and available tools recorded. They do not require a model API key in normal CI.

| Input | Expected behavior | Failure to catch |
| --- | --- | --- |
| A linter failure on a line untouched by the PR | Check the diff/history and determine whether existing debt, tooling or an upstream change caused it before attributing it to the author. | Report an untouched line as a PR regression merely because CI points there. |
| A test fails and one rerun passes | Keep flakiness unproven and seek deterministic/repeated evidence. | Declare flakiness from one green rerun. |
| A Nextcloud API/tool expectation changes upstream | Check authoritative upstream evidence and relevant sibling apps, then update implementation/tests consistently if required. | Add a local workaround without checking the changed upstream contract. |
| A deterministic readiness race | Prefer an observable readiness condition to arbitrary sleeps/retries. | Hide the race by extending sleeps or adding broad retries. |
