<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Git commit identity and DCO

Before creating any Git commit through GitHub, a repository connector, a CLI, or another tool:

1. Include a DCO `Signed-off-by: <name> <email>` trailer in every commit.
2. Use the interacting user's configured DCO identity when it is available in trusted user context or the execution environment.
3. Never infer, invent, normalize, or substitute the user's DCO name or email from a GitHub username, account profile, commit author, repository metadata, or another person's identity.
4. If no DCO identity is available, ask the interacting user for the name and email before creating the first commit.
5. Preserve that confirmed identity for subsequent commits in the same task unless the user changes it.
6. When local Git is available, prefer `git commit -s` with the intended `user.name` and `user.email`. When a repository tool accepts only a commit message, append the exact `Signed-off-by` trailer manually.

Do not create an unsigned commit first and plan to repair it later.
