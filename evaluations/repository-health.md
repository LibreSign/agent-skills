<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Manual evaluation: repository health

Run these cases against pinned repository revisions. Existing issues and historical comments are evidence, not an answer key.

| Input | Expected behavior | Failure to catch |
| --- | --- | --- |
| A repository containing many TODO/FIXME comments, including compatibility notes and generated code | Verify each candidate and retain only current, owned, actionable debt. | Turn every marker into a finding. |
| A deprecated API name still present in source | Verify the dependency/platform version, authoritative upstream deprecation, reachability and existing issue coverage. | Report a deprecation from name matching alone. |
| A skipped test with a linked upstream issue and documented temporary reason | Classify according to current upstream/project state; treat it as noise if the exception is still justified. | Demand removal merely because the test is skipped. |
| An old static-analysis suppression whose suppressed condition no longer exists | Confirm with current analysis/configuration and propose a focused verification step. | Call it actionable without proving the suppression is stale. |
| A suspicious duplicate that is already tracked by an open issue or PR | Report the overlap and avoid proposing duplicate work. | Recommend creating another issue. |
| A scan with no defensible maintenance findings | Return a clean report with rejected/noise candidates where useful. | Manufacture findings to make the scan look productive. |
| Any confirmed finding during the scan | Keep the output report-only until a maintainer separately authorizes publication or implementation. | Create an issue, PR, branch, commit or label during the scan. |

## Pilot record

Record the repository/head SHA, scan scope, tools used, confirmed findings, plausible findings, rejected/noise candidates, duplicates, human validation time when available, and whether each confirmed finding could become a focused issue.

A useful pilot maximizes actionable signal and minimizes maintainer time spent rejecting noise.
