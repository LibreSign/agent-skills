<!-- SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
     SPDX-License-Identifier: AGPL-3.0-or-later -->

# Coordinator/subagent pilot

Use this protocol only when evaluating whether temporary delegation improves `execute-issue`. It is not a new skill and does not make multi-agent execution the default.

## Runtime requirement

Use a runtime that provides genuinely separate subagent contexts. The OpenAI Agents API is one supported runtime: enable `agent.multi_agent.enabled` for the coordinated run. The managed harness supplies subagent creation, messaging, waiting and interruption; do not emulate this with repeated sequential prompts.

Official references:

- https://developers.openai.com/api/docs/guides/agents-api/multi-agent
- https://developers.openai.com/api/docs/guides/agents-api/overview

For the controlled baseline, use `environment.type = none` and provide one self-contained task packet. This keeps the pilot read-only and removes repository/environment differences from the comparison. A later repository-execution pilot may use a supported hosted or self-hosted environment, but that is a separate experiment.

## Comparable runs

Run the exact same:

- task packet;
- model;
- coordinator instructions except for the delegation instruction;
- evaluation rubric.

The single-flow run must omit multi-agent configuration. The coordinated run should enable multi-agent with a small explicit limit, normally two subagents for the first trial.

The task must contain at least two genuinely independent questions. Do not force delegation on a sequential task just to make the multi-agent run look active.

## Evidence to record

Record automatically when available:

- model;
- wall-clock duration;
- subagent creation events and IDs;
- final output;
- token/usage fields exposed by the runtime;
- raw event types needed to diagnose handoffs.

Score manually:

- completion correctness;
- human interventions;
- duplicated investigation;
- handoff failures;
- whether the coordinator verified conflicting subagent evidence.

A multi-agent run only wins when it reduces coordination cost or latency without reducing correctness.

## Safety and publication

Use a synthetic or intentionally shareable task packet for the first API pilot. Do not put credentials, private issue content, embargoed vulnerabilities or unrelated user data into the fixture.

The pilot is read-only. It must not publish issues, PR comments, commits or repository changes.

## Runner

`evaluations/orchestration_pilot.py` executes the controlled pair of runs. It requires:

- the current OpenAI Python SDK;
- `OPENAI_API_KEY`;
- an explicit `--model`;
- a task packet passed through `--input`.

The result JSON intentionally leaves correctness and human-intervention fields empty for maintainer review rather than inventing them.
