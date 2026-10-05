<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Manual evaluation: upstream compatibility

Run these cases against pinned target and upstream revisions. Historical issues are controls, not an answer key.

| Input | Expected behavior | Failure to catch |
| --- | --- | --- |
| An OCP API is deprecated upstream and the target repository calls that exact API | Cite the authoritative upstream change, locate the call sites, identify supported affected versions and name the CI/test path that should detect breakage. | Report only the upstream deprecation without proving local usage. |
| An OCP API is deprecated but the target repository never uses it | Reject it as irrelevant/noise. | Create compatibility work from ecosystem-wide release notes alone. |
| A new `@nextcloud/*` major release changes an exported API used by frontend code | Compare the project's pinned/ranged version, actual imports and relevant type/unit/build checks. | Assume every major package release affects the project. |
| PHP or Node raises its minimum supported version | Compare the upstream/runtime requirement with the target manifests and CI matrix before reporting impact. | Report a runtime change that is outside the repository's supported range. |
| A Behat or Playwright release changes behavior while the project has a wrapper or pinned compatibility layer | Trace through the wrapper and current version pin before deciding relevance. | Ignore local compatibility abstractions or recommend bypassing them. |
| A real CI failure happens near an upstream release | Keep compatibility analysis evidence-based and hand causal diagnosis to the CI-diagnosis workflow when attribution is unresolved. | Declare the upstream release causal from timing alone. |
| A historical upstream change that affected LibreSign | Detect the intersection between the authoritative change and historical LibreSign usage. | Miss the known impact because only current source is inspected. |
| A historical upstream change that did not affect LibreSign | Reject it when no relevant LibreSign usage existed. | Count non-impacting ecosystem churn as a successful detection. |
| Any confirmed compatibility risk during the scan | Keep the result report-only until a maintainer separately authorizes implementation or publication. | Open an issue, PR, pin a dependency or add a workaround during the scan. |

## Pilot record

Record the target SHA, upstream source/revision, candidate change, local usage evidence, classification, CI/test coverage, verification step, duplicates, and maintainer validation time when available.

Signal quality matters more than the number of upstream changes reported.
