<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Evidence-first testing for reviews and fixes

Use these principles when a code review, issue or CI diagnosis raises a possible defect. This is a verification workflow, not a requirement to practice full test-driven development for every change.

## Establish a falsifiable case

1. Identify the project's actual contract and a reachable input, role, state or configuration. Check the producer and consumer of the data; do not create an impossible mock payload to justify a fix.
2. State the expected **observable behavior** and the result that would disprove the hypothesis. Select the smallest useful test level (unit, integration, contract or end-to-end) for the boundary involved.
3. Inspect existing tests and CI execution first. A passing suite proves only that the executed assertions passed; it may omit the candidate path. A skipped job is not positive evidence.
4. When feasible and safe, run a focused test against the current implementation. Confirm that a failure is caused by the claimed behavior, not invalid setup, an unrelated assertion or an unavailable service. A negative test must reject the wrong behavior; a positive control must still accept valid behavior.
5. If the case fails for the expected reason, request or implement the smallest correction, retain the test, rerun it to confirm the fix, and run neighboring regression checks. If it passes, examine whether the assertion is sensitive enough and then reconsider or discard the finding. If it cannot run, label the conclusion as unverified.

A confirmed breach of a verified contract can also be demonstrated with other strong evidence (for example, a reproducible execution trace). Do not make a newly committed failing test an unconditional prerequisite to reporting security or data-integrity risks. Keep sensitive reproductions out of public comments.

## Use parameterization deliberately

- Prefer named independent cases for inputs that share the **same** setup, action, contract and expectation. Examples: PHPUnit `#[DataProvider]`, Vitest `it.each`, and an existing project's scenario outline. Each dataset should identify the exact failing case.
- Consider boundary and malformed values, null/missing fields, relevant roles and workflow states, plus a valid control. Select only variants that can occur under the real interface or are deliberately tested as untrusted inputs.
- Do not parameterize unrelated user journeys or move complicated logic into fixtures just to reduce duplication. Keep expected results explicit; avoid deriving them from the code under test.
- Assert observable outputs, effects and access boundaries, not incidental internal call counts, source-file names or coverage percentages. For privacy, the absence of an unauthorized field may matter more than a neutral-looking UI label.

## Match the recommendation to the evidence

- **Confirmed defect:** describe the contract violation, effect and proof; ask for a focused fix and lasting test coverage.
- **Plausible defect:** ask for a focused reproducer or test with expected results and a valid control; make a production change conditional on its outcome. Do not automatically request changes for every hypothesis.
- **Disproved or redundant claim:** drop the finding instead of generating noise.
- **Inconclusive high-risk boundary:** explain why validation is needed before merging without calling the defect proven.

## Selected references

- Martin Fowler, [Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html): test-first development and red-green-refactor as a useful method, not a compulsory ritual for review.
- Google Testing Blog, [Test Behaviors, Not Methods](https://testing.googleblog.com/2014/04/testing-on-toilet-test-behaviors-not.html) and [Keep Tests Focused](https://testing.googleblog.com/2018/06/testing-on-toilet-keep-tests-focused.html): test externally meaningful behavior and keep independent scenarios readable.
- Google Testing Blog, [Tests Too DRY? Make Them DAMP!](https://testing.googleblog.com/2019/12/testing-on-toilet-tests-too-dry-make.html): favor clarity over excessive reuse in test code.
- PHPUnit, [Writing Tests: Data Providers](https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html#data-providers) and Vitest, [`test.each`](https://vitest.dev/api/test.html#test-each): independently reported parameterized cases where appropriate for the project's installed version.
- ISTQB, [Confirmation Testing](https://glossary.istqb.org/en_US/term/confirmation-testing): rechecking a corrected defect is distinct from running broader regression checks.
