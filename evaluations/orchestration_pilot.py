# SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Run a controlled single-flow vs multi-agent Agents API pilot."""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

BASE_INSTRUCTIONS = """Use the supplied task packet only. This is an evaluation run: do not publish, modify repositories, or perform external actions. Analyze the task, separate facts from hypotheses, and return a concise engineering report with: findings, evidence, unresolved questions, and recommended next step."""

COORDINATION_INSTRUCTIONS = BASE_INSTRUCTIONS + """
Use temporary subagents only for genuinely independent investigation. Delegate at least two independent questions when the task packet supports that split, wait for their results, verify them, and synthesize one answer. Keep dependent steps in the coordinator."""


def session_kwargs(model: str, task: str, coordinated: bool, max_subagents: int) -> dict[str, Any]:
    agent: dict[str, Any] = {
        "model": model,
        "instructions": COORDINATION_INSTRUCTIONS if coordinated else BASE_INSTRUCTIONS,
    }
    if coordinated:
        agent["multi_agent"] = {
            "enabled": True,
            "max_concurrent_subagents": max_subagents,
        }
    return {
        "agent": agent,
        "environment": {"type": "none"},
        "input": task,
        "stream": True,
    }


def dump_model(value: Any) -> Any:
    if value is None:
        return None
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if isinstance(value, (str, int, float, bool, list, dict)):
        return value
    return str(value)


def run_once(client: Any, *, model: str, task: str, coordinated: bool, max_subagents: int) -> dict[str, Any]:
    started = time.perf_counter()
    event_types: list[str] = []
    subagent_ids: list[str] = []
    raw_events: list[Any] = []

    with client.beta.agents.sessions.create(
        **session_kwargs(model, task, coordinated, max_subagents)
    ).with_result_collection() as stream:
        for event in stream:
            event_data = dump_model(event)
            raw_events.append(event_data)
            event_type = event_data.get("type") if isinstance(event_data, dict) else None
            if event_type:
                event_types.append(event_type)
            if event_type == "agent.session.subagent.created" and isinstance(event_data, dict):
                subagent_id = event_data.get("subagent_id") or event_data.get("id")
                if subagent_id:
                    subagent_ids.append(str(subagent_id))
        result = stream.get_final_result()

    elapsed = time.perf_counter() - started
    result_data = dump_model(result)
    usage = result_data.get("usage") if isinstance(result_data, dict) else None
    output_text = getattr(result, "output_text", None)
    if output_text is None and isinstance(result_data, dict):
        output_text = result_data.get("output_text")

    return {
        "mode": "coordinated" if coordinated else "single",
        "model": model,
        "wall_clock_seconds": round(elapsed, 3),
        "subagent_count": len(set(subagent_ids)),
        "subagent_ids": sorted(set(subagent_ids)),
        "event_types": event_types,
        "usage": usage,
        "output_text": output_text,
        "events": raw_events,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True, help="Task packet used for both runs")
    parser.add_argument("--model", required=True, help="Agents API model id")
    parser.add_argument("--output", type=Path, required=True, help="JSON result path")
    parser.add_argument("--max-subagents", type=int, default=2)
    args = parser.parse_args()

    if args.max_subagents < 1:
        parser.error("--max-subagents must be >= 1")
    if not os.getenv("OPENAI_API_KEY"):
        parser.error("OPENAI_API_KEY is required")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise SystemExit("Install the current OpenAI Python SDK before running this pilot") from exc

    task = args.input.read_text()
    client = OpenAI()
    single = run_once(client, model=args.model, task=task, coordinated=False, max_subagents=args.max_subagents)
    coordinated = run_once(client, model=args.model, task=task, coordinated=True, max_subagents=args.max_subagents)

    record = {
        "task_file": str(args.input),
        "single": single,
        "coordinated": coordinated,
        "manual_metrics": {
            "single_correctness": None,
            "coordinated_correctness": None,
            "single_human_interventions": None,
            "coordinated_human_interventions": None,
            "duplicated_work_notes": None,
            "handoff_failure_notes": None,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
