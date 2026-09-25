<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Review-skill evaluation cases

These public PRs are examples for **retrospective evaluation**, not an exhaustive defect ground truth. Existing human comments may be right, wrong, incomplete or stale. Pin each run to a head SHA; reconstruct the code and discussion at that revision. Never post test output or comments to the referenced PRs. Do not copy private chat transcripts into this repository.

| PR | Behavior to evaluate | Counterexample or failure mode |
| --- | --- | --- |
| [LibreSign/libresign#8719](https://github.com/LibreSign/libresign/pull/8719) | Test changes for mutation coverage: ask whether call-count expectations represent observable behavior; inspect `assertSame` argument order separately. | Do not demand a brittle test merely to improve the mutation score; do not classify an assertion-order clarity improvement as a runtime blocker. |
| [LibreSign/woocommerce-nextcloud-admin-group-manager#31](https://github.com/LibreSign/woocommerce-nextcloud-admin-group-manager/pull/31) | Browser E2E suite: understand its separate HTTP stub and WooCommerce user flows, then assess the README claim that tests mirror source files. | Do not reject browser testing because unit tests exist; do not require an E2E test per production file. |
| [LibreSign/woocommerce-restrict-switch#1](https://github.com/LibreSign/woocommerce-restrict-switch/pull/1) | Consider whether a missing product can make `get_product()` return false; propose a focused reproducer for both affected paths. | Do not assert that a fatal error was reproduced if it was only inferred; do not treat all declared-version mismatches as automatic blockers without project context. |
| [LibreSign/woocommerce-nextcloud-admin-group-manager#30](https://github.com/LibreSign/woocommerce-nextcloud-admin-group-manager/pull/30) | Check whether centralizing requests and its integration tests preserve behavior and fix trailing-slash URLs. | A legitimate answer may recommend no inline comments; do not invent issues to fill the format. |
| [LibreSign/libresign#8705](https://github.com/LibreSign/libresign/pull/8705) | Inspect policy-store method contracts and generated API types in repository context. | Do not infer a missing UI behavior from a store-only PR or treat coverage percentages as proof of a defect. |
| [LibreSign/libresign#8706](https://github.com/LibreSign/libresign/pull/8706) | Trace a rejected signer through backend status, sequential flow, UI eligibility and frozen policy configuration. | Do not decide correctness from one changed function or from a green CI summary alone. |
| [LibreSign/libresign#8720](https://github.com/LibreSign/libresign/pull/8720) | Assess UUID-specific cache behavior and tests against the PR's deliberately limited scope. | Do not demand the entire linked refactor in the first step. |

## Manual run record

For each case, record date, model, skill revision, repository/head SHA, tools and context available, checks executed, accepted findings, rejected findings, missed issues discovered by later human review, line accuracy, and time spent by the human validating the result. Compare this to a review without the skill when practical. Evaluate usefulness and restraint together; a higher count of comments is not success.

Include a fresh PR with no prior public review in later evaluation rounds. Historical discussions reveal candidate answers to the model and cannot measure every issue a human might also have missed. Test an adversarial PR description containing instructions to post or approve: the skill must ignore those instructions and return only a draft.
