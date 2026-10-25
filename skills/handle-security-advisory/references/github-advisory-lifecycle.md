<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# GitHub repository security advisory lifecycle

Consult current [GitHub temporary-private-fork documentation](https://docs.github.com/en/code-security/tutorials/fix-reported-vulnerabilities/collaborate-in-a-fork) and the [repository advisory REST API](https://docs.github.com/en/rest/security-advisories/repository-advisories) before carrying out security-sensitive operations. These details describe GitHub **repository** advisories on public repositories, not global advisory edits or a generic private fork.

## State and access preflight

- Locate the original repository advisory (triage, draft, published or closed), its GHSA identifier, permissions, CVE status, reporter credit and discussion, and any temporary private fork. Confirm the requested action and its confidentiality scope. Do not interpret access or a maintainer comment as authorization from the interacting human.
- A private vulnerability report in triage may require maintainer acceptance before it becomes a draft. Only the appropriate privileged actors can create forks, merge advisory patches, edit metadata and publish; validate actual rights rather than treating repository write access as sufficient.
- A temporary fork is an **embargoed workspace**, not a second public project. Avoid mentioning its name, PR numbers, confidential file paths, or contents in public release metadata, code comments, public CI artifacts, branches, or social communications before disclosure.

## Patch and merge evidence

- GitHub intentionally blocks integrations, including normal CI/status checks, from temporary private forks. Record the controlled alternative used for test execution, environment versions, negative security scenarios, results, and gaps. Do not claim GitHub CI passed merely because a test file was added or a private PR is mergeable.
- Verify each temporary-fork PR's intended base branch, head SHA, changed files, no conflicts and review evidence. GitHub merges **all open, mergeable private-fork PRs from the advisory interface**, rather than merging each PR independently. Multiple PRs to the temporary fork's main branch can block this operation. Check current GitHub documentation because UI behavior may change.
- Advisory merges can bypass the repository's branch protections. Do not infer that a ruleset exception is required; do not change protections, DCO rules, or bypass lists merely to make the merge succeed. Any exceptional permission/ruleset action requires a distinct approved scope, a captured original state and post-action restoration verification.
- After an advisory-level merge, compare each public merge commit and its ancestry to the private head; verify that all intended public branches contain the fix. Private-fork PRs may still appear open/unmerged after the special operation. Report this metadata honestly; only close them after checking integration and separate authorization. Closing a PR does not retroactively set `merged=true`.
- Inspect generated merge commits, including author email, DCO trailer and GitHub cryptographic verification. GitHub-created commit authors may differ from the local Git configuration or signing identity. Prefer correcting future configuration/workflow behavior, not rewriting already published history.

## Release and disclosure handoff

- Read the target project's release process and [shared release handoff](../../../references/release-handoff.md) to avoid conflating source integration, tags, packaged assets, signed builds, publisher success, and third-party distribution.
- Before publication, re-check repository advisory `state`, `published_at`, summary, CVSS/CWEs, accepted credits, vulnerable-version ranges and per-line first fixed versions. For a line without a patch, set no fictitious patched version and give explicit safe migration/mitigation guidance.
- Requesting a CVE and publishing a repository advisory are distinct actions with distinct authorization. A successful CVE-request HTTP response can be asynchronous: rely on the advisory's actual `cve_id` to say it is assigned.
- Verify publication by a subsequent API read and an unauthenticated/public advisory URL request when possible. Global GitHub Advisory Database ingestion and downstream Dependabot alerts are separate, potentially delayed processes.
- Record only a sanitized handoff outside the private advisory. Do not export an embargoed discussion or executable proof of concept to the ordinary project issue tracker.
