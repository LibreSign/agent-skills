<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Quality and relationships

## Scope before structure

Use an issue when one contributor can deliver and verify the outcome as a coherent change. Use an epic when several deliverables share an outcome and a maintainer needs to track their progress. Prefer small independent issues that can be tested and reviewed; split when separate user-facing outcomes, stable contracts, or oversized changes make that practical. Do not fragment an operation into untestable setup steps or invent long dependency chains just to create more newcomer labels. An epic with no actionable children is a planning gap, unless the user explicitly wants an initial discovery proposal.

Inspect the target repository's source, tests, issue history and versioned contracts before making detailed implementation claims. Cite relevant issue or code references in the body when they help the implementer; avoid stale line numbers or copied private discussions. Preserve the origin of the request so later contributors understand why the work exists.

A useful issue states what should be true when done, where current behavior differs, why it matters, boundaries and risks, concrete acceptance criteria, how to verify the outcome, and what is out of scope when ambiguity is likely. Use clear, plain language and short sections; retain necessary technical precision. Include file names, APIs, commands or target release only after checking them. Specify project ownership of security checks: a frontend change must not silently replace required server-side authorization. Avoid prescribing the same input check at every forwarding layer when the responsible boundary already enforces it.

For work shared across backend and frontend, document the source of truth, endpoints or events, request and response shape with examples, permission and validation rules, errors, state transitions and compatibility expectations **only where each is relevant and verified**. If that contract does not exist yet, make agreeing and testing it a clear backend deliverable. Frontend UI and mocked contract tests may proceed against the agreed contract; only integration truly blocked by the backend should have a `blocked by` link. State the handoff and integration tests, including what must be reconciled after parallel work.

Every implementation issue needs an appropriate test path. Inspect the project's actual CI and test architecture before naming commands: unit and integration tests for behavior and security boundaries, browser tests such as Playwright for important user flows where the project uses them, and required type, lint and other static checks. Ask for a test that would fail under the wrong behavior, not a list of tools for appearance. For UI changes, request a screenshot or short video with the implementation PR to aid review, and avoid exposing personal or sensitive data in captures. A visual artifact supports review; it does not replace automated behavior tests.

For `good first issue`, verify that prerequisites are available and the contract, affected area and tests are clear enough for a newcomer; the label reflects approachability, not merely short length. Do not label an entire complex epic just because a child is approachable. Use project-specific closing text, support links, templates and metadata only when the project uses them.

For domain-specific features, research relevant free implementations and public documentation from proprietary products when they clarify user expectations or interoperability. Label what is directly observed, what the documentation promises and what is only an inference. Competitor behavior is evidence for a choice, not a substitute for the target project's requirement or a normative standard. Reread each draft from an implementer's perspective, then recheck every factual claim and proposed test against code and current project configuration.

## Relationship decisions

| Relationship | Test | Representation |
| --- | --- | --- |
| Parent / sub-issue | Is completion of the child part of the parent's outcome? | Use GitHub's native sub-issue relation where available; include a contextual link in the body only when helpful. |
| Blocked by | Could this issue be correctly completed without the other issue being completed? | Add the native dependency in the correct direction if the answer is no. Do not block merely because the other issue is related. |
| Related | Does the other issue provide context without being a prerequisite or part of the outcome? | Link as context, without inventing hierarchy or blocking. |

Check existing relationships before planning new ones. Dependencies can cross repositories when supported and justified; a sub-issue belongs under the epic whose outcome contains it. Avoid circular or redundant edges, and identify which children can proceed in parallel. Project boards, issue types, priorities, labels and milestones differ across projects: use live repository conventions, not a universal mapping of “epic” to a GitHub type or label.

Do not make public issue bodies into vulnerability disclosure reports. If an issue concerns a sensitive weakness, use the project's private security reporting policy and keep any public tracking text non-exploitable.
