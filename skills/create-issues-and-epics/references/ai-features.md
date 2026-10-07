<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# AI feature planning

Use this reference only for AI-assisted product work.

## Product boundary

Treat AI as a tool over implemented product capabilities, not as a replacement for deterministic domain behavior. Prefer deterministic code when the problem can be solved reliably without AI. Separate:

- **system guarantees**, which normal application code must enforce, from
- **AI objectives**, which are probabilistic suggestions, summaries, classifications, drafts or extracted information.

Do not make model output the authority for permissions, policy resolution, cryptographic validity, legal validity, access control, workflow state or other deterministic security/domain decisions.

## Human authority and agency

Classify the consequence of the AI-assisted action. Informational output such as summaries or drafts may need review but normally does not mutate state. Suggestions that create or modify domain objects require normal validation and explicit acceptance. External or destructive actions require application authorization and, where appropriate, explicit human confirmation.

Give models the minimum data, tools and permissions required for the requested operation. A model may propose an action; the normal application service must validate actor, policy, object state and parameters before execution.

## Trust boundaries

Treat source documents, retrieved context and model output as untrusted data. Plan defenses for prompt injection, malformed structured output, unsafe generated markup, tool misuse, data leakage and cross-user authorization failures. Keep business rules and access control outside prompts.

When the feature summarizes or explains a source document, keep the source document authoritative. Prefer provenance or navigation back to supporting source locations when the platform/provider can supply them; do not promise citations that the actual capability cannot produce.

## Provider and platform ownership

Use the target platform's public AI abstraction when one exists instead of creating a parallel provider/model registry. Keep provider credentials, endpoint/model selection and provider lifecycle in the platform layer unless the product explicitly owns them.

Do not infer that a provider is private, local, trustworthy or ethically rated from its app/model name. Surface only metadata the platform exposes through a supported public contract. If desired trust/privacy metadata is unavailable, record it as a deferred/upstream-dependent question rather than building brittle heuristics.

## Policy and transparency

Make AI use subject to the application's existing authorization and policy model. Capability availability answers whether the system *can* perform an operation; policy answers whether the actor *may* perform it.

Make AI-assisted behavior identifiable to users. Document intended use, material limitations, relevant data-processing implications, prerequisites, and the authoritative role of normal product/domain rules.

## UX

Research the existing product flow and relevant ecosystem patterns. Prototype new or consequential interactions before implementation when placement, terminology, disclosure, review/acceptance, source navigation, or error recovery is not obvious. Favor progressive disclosure and keep AI assistance subordinate to the primary task.

## Tests

Require deterministic tests that do not depend on paid external AI. Cover capability absence, policy denial, malformed/hostile input, invalid model output, cancellation/failure and normal validation. Add provider/integration smoke tests only where they add confidence without making ordinary CI flaky or costly.

For probabilistic real-model tests, assert stable contracts and invariants (successful completion, non-empty/parseable shape, authorization, validation) rather than exact generated prose.

## Planning

Do not fully decompose downstream AI epics before blocking domain/platform contracts are stable. Preserve benchmark research and open questions, then use the upstream epic's completion handoff to revise assumptions and create focused implementation issues.
