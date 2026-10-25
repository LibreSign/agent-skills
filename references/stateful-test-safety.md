<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Safety for tests with mutable or destructive state

Use this preflight only for checks that can modify files, databases, global application config, queues, external services, or permissions. A passing test is not proof that its environment was safe.

1. Identify the precise mutation targets, cleanup hooks, credentials and runtime process. Verify that the paths, database/schema, volumes, ports, app config and service connections are test-owned or disposable. Do not run destructive tests against a shared Nextcloud installation or another worker's state.
2. Use the target repository's canonical isolated environment. Prefer separate worktrees/containers plus distinct persistent volumes and configuration; isolation in one Docker daemon is not a security sandbox for hostile code. Avoid privileged containers and production credentials.
3. For integration tests changing persistent state, snapshot only the relevant pre-test values and restore them in a reliable teardown/finally path; preserve absent-vs-empty and types. Verify cleanup under failing assertions as well as successful tests. Prefer transaction rollback where it covers all affected state.
4. For tests of cleanup, migration, backup, directory-copy, process management or filesystem permissions, use disposable synthetic fixtures and assert that paths resolve within the intended sandbox before any deletion. Do not rely solely on a lexical string-prefix check where traversal or symlinks are possible.
5. Confirm the environment is still clean afterward. A second run should not depend on the first; report any remaining mutation and stop before running broader suites.
6. If isolation cannot be proven, do not run the destructive test. Use static analysis, mocks or a prepared test plan and disclose that runtime verification was not performed.

Run ordinary source-only/unit tests without imposing a Docker startup by default. These controls apply to the risk of the test, not to every repository task.
