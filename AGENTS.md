<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Working on this repository

- Keep each skill's `SKILL.md` focused on activation and the essential workflow. Put optional detail in directly linked `references/` files.
- Keep the review skill applicable to different repositories. Read the target repository's own instructions at review time; do not copy changing product facts here.
- Treat a change to instructions as a change in reviewer behavior. Explain which evaluation case it improves, and check a clean counterexample for added noise.
- Do not add automatic publishing of PR comments, reviews, issues, labels, commits or CI reruns to `review-pull-request`. Its default operation is read-only on the reviewed repository. A human must see and authorize the exact external action before it occurs.
- Do not commit private chat history, credentials, private PR content, or sensitive vulnerability details. Public evaluation cases may link to public PRs but should summarize decision patterns rather than copy discussions wholesale.
- Preserve the package layout and validate `plugin.json`, skill frontmatter, reference paths and Markdown examples before proposing changes. Run the checks and consult `CONTRIBUTING.md` for how behavior is evaluated.
