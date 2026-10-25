<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Security advisory disclosure preflight

Use this checklist when drafting a public security advisory, evaluating publication readiness, or reviewing a published advisory. This is a decision aid, **not** authorization to publish.

## Evidence and wording

- Name the affected product/component and the vulnerability class. Describe exploit prerequisites (network, authentication, role, configuration, user interaction) and actual impact without minimizing severity.
- Separate a reporter's demonstrated result, maintainers' independent verification, code-only inference on other release lines, and untested possibilities. Avoid saying an exploit or integration test was reproduced on a version when only source code was inspected.
- Preserve the underlying restricted report, evidence, attribution, and technical audit trail. Public descriptions can link to code changes and regression tests without distributing a weaponized payload against still-unpatched installations. Do not erase evidence to improve public relations.
- Confirm CVSS vector/score, CWE categories, and reporter credit/acceptance with the actual advisory metadata. An advisory can be published without a CVE; a request in progress is not an assigned identifier.

## Affected users and fixes

- Validate first affected versions, range syntax per applicable package ecosystem, branch-to-product-version mapping, and first patched versions against tags and code. Avoid ambiguous open-ended version ranges that incorrectly classify future fixed releases as vulnerable.
- Check the target project's real support policy, stable/EOL schedule and the latest release status upstream. Clearly distinguish unfixed EOL lines and public package availability from support promises. A paid exceptional support option is mentioned only when the project actually offers it; never invent backport commitments, SLAs, timelines or guarantees.
- Confirm branch fix containment, public release tag, package integrity/signatures, publisher workflow result and channel visibility (if available). A GitHub release alone does not prove that a package reached users.
- Give a version-specific update or migration recommendation. Describe partial mitigations as partial, and avoid presenting disabling one affected endpoint as a complete workaround when other paths remain.

## Disclosure, trust and business language

- Treat timing as coordinated with the reporter and project policy; a common disclosure window is not inherently a minimum embargo. Do not publish before any expressly agreed embargo or other applicable disclosure commitment without resolving it.
- Verify every support email, product link and contact from the organization's official public documentation or directly from the interacting human. Do not assume the brand or commercial provider of an unrelated project.
- Separate openly available patches from optional paid professional services. State commercial terms conditionally, avoid implied entitlements and contractual promises, and do not turn the vulnerability description into sales copy.
- Review public links and text for credentials, internal hosts, private repository references, customer identifiers, confidential code, excessive exploit detail and misleading test claims.

## Gates and aftercare

- **Prepare:** show the exact proposed public summary, impact, affected versions, fixed versions, remediation, credits, caveats and unresolved gaps for review.
- **Patch/release:** explicitly request authority for each modifying/merging/release action if not already approved.
- **Publish:** require express authorization of the public disclosure; re-read the live metadata immediately beforehand. If a fix is unavailable for any affected line, explain the consequence and the recommended upgrade path before publication.
- **Verify:** re-read the advisory after publication, confirm a public URL, and distinguish GitHub's acknowledgement of a CVE request from actual assignment and database indexing.
- **Handoff:** record publication URL, release evidence, affected EOL exposure, reporter communication status and outstanding CVE/index tasks. Never claim completion of unverified follow-up work.
