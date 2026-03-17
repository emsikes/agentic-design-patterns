# Chapter 5 — Tool Use / Function Calling

## Pattern Overview

Tool use gives agents the ability to take actions beyond text generation — calling functions, querying APIs, performing calculations, retrieving data. The agent reasons about which tool to use, executes it, incorporates the result, and continues reasoning. This transforms an agent from a text generator into an actor that can interact with the world.

**Core insight:** An LLM alone can only reason about what it knows. Tools extend that capability to real-time information retrieval, computation, and external system interaction. The agent decides when and which tool to call based on the task — tool selection is itself a reasoning step.

## Framework

**CrewAI** — First chapter using CrewAI. The framework organizes everything around three primitives: Agents, Tasks, and Crews. An Agent has a role, goal, and backstory. A Task has a description and expected output assigned to an agent. A Crew orchestrates execution. Even a single-agent project follows this structure — it's the foundation for multi-agent collaboration in Ch 7.

## Our Implementation

**Mini-project:** Research Assistant Agent

A single Research Assistant agent equipped with three tools — web search, calculator, and Wikipedia lookup — answers a research question requiring both factual retrieval and numerical computation.

```
question → agent reasons → selects tools → executes → reasons → final answer
```

Tools used in this run:
- `web_search` — called first for current state of quantum computing
- `calculator` — computed `(1E9-1E6)/1E6*100 = 99900.0` correctly
- `wikipedia_lookup` — attempted as fallback when web search failed

## File Breakdown

| File | Responsibility |
|---|---|
| `tools.py` | Three `@tool` decorated functions — web search, calculator, Wikipedia lookup |
| `agent.py` | Defines the `researcher` Agent with role, goal, backstory, and tool list |
| `task.py` | `create_research_task()` — binds a question to the researcher agent |
| `crew.py` | `build_crew()` — assembles agent and task into a sequential Crew |
| `main.py` | Entry point — defines question and calls `crew.kickoff()` |

## Key Concepts

**`@tool` decorator:** Converts a plain Python function into a CrewAI tool. The function name becomes the tool identifier and the docstring is passed to the agent as the tool description — the agent reads it to decide when to use the tool. Clear, specific docstrings are critical for good tool selection.

**Role / Goal / Backstory:** CrewAI's agent definition triad. Together they replace what LangGraph handles through graph structure and what AutoGen handles through system messages. The backstory is particularly important — it shapes how the agent approaches ambiguous situations.

**`Process.sequential`:** CrewAI's execution mode for running tasks one after another. Relevant when multiple agents are involved (Ch 7). Even with one agent it must be specified explicitly.

**`crew.kickoff()`:** CrewAI's equivalent of `graph.invoke()` — starts execution and returns the final output.

**Tool isolation:** CrewAI manages its own OpenAI client internally. Tools that make API calls must instantiate their own `OpenAI()` client inside the function body — a module-level shared client conflicts with CrewAI's client management and produces a `cached_property` error.

## Observed Behavior

- Agent correctly selected `web_search` and `calculator` in parallel on the first reasoning step
- Calculator correctly computed `(1E9-1E6)/1E6*100 = 99,900%`
- Web search and Wikipedia tools failed due to client isolation issue (fixed by moving client instantiation inside each tool function)
- Agent gracefully degraded — acknowledged tool failures and synthesized a coherent answer from internal knowledge
- The graceful degradation behavior is a key property of well-designed tool use agents

## CrewAI vs LangGraph vs AutoGen

| | LangGraph | AutoGen | CrewAI |
|---|---|---|---|
| Mental model | Graph — nodes and edges | Conversation — agents and messages | Roles — agents, tasks, crews |
| Tool definition | Python functions + manual wiring | Function schemas | `@tool` decorator with docstring |
| Execution trigger | `graph.invoke()` | `initiate_chat()` | `crew.kickoff()` |
| Best for | Stateful pipelines | Agent conversation loops | Role-based multi-agent workflows |

## Running It

```bash
cd agentic-design-patterns
source .venv/bin/activate
python ch05_tool_use/main.py
```
