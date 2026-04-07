# Chapter 7 — Multi-Agent Collaboration

## Pattern Overview

Multi-agent collaboration divides a complex goal across specialized agents, each owning a distinct role and stage of the pipeline. Rather than one agent doing everything, work is handed off sequentially — each agent receives the previous agent's output as context and contributes their specialized expertise before passing to the next.

**Core insight:** A single agent asked to research, write, and edit a blog post produces generic output at every stage. Three specialized agents — each with a focused role, goal, and backstory — produce meaningfully better results because each LLM call is optimized for one job. Division of labor applies to agents just as it does to human teams.

**Multi-Agent Collaboration vs Tool Use (Ch 5):**
- Ch 5: One agent, extended capabilities through tools
- Ch 7: Multiple agents, each owning a distinct stage of the pipeline
- Tool use augments what one agent can do. Collaboration divides what needs to be done.

## Framework

**CrewAI** — The framework's native strength. Three agents (Researcher, Writer, Editor) collaborate via `Process.sequential`. CrewAI automatically passes each completed task's output as context to the next task in the list — no explicit wiring required. List order drives handoff order.

## Our Implementation

**Mini-project:** Content Production Team

Three specialized agents produce a polished technical blog post on agentic AI systems and their impact on software development.

```
topic → Researcher → research brief → Writer → draft post → Editor → final post
```

## File Breakdown

| File | Responsibility |
|---|---|
| `agents.py` | Defines three `Agent` instances — researcher, writer, editor — each with distinct role, goal, and backstory |
| `tasks.py` | `create_tasks(topic)` — returns ordered list of three tasks, one per agent |
| `crew.py` | `build_crew(topic)` — assembles agents and tasks into a sequential Crew |
| `main.py` | Entry point — defines topic and calls `crew.kickoff()` |

## Key Concepts

**Sequential context passing:** With `Process.sequential`, CrewAI automatically injects each completed task's output into the next task's context. The writer task doesn't need an explicit reference to the research brief — CrewAI passes it implicitly. List order in `create_tasks()` determines handoff order.

**Process.sequential vs Process.hierarchical:**
- `sequential` — fixed task order, output flows down the list. Default mode.
- `hierarchical` — a manager agent dynamically assigns tasks. More flexible, more expensive (extra LLM call per assignment decision).

**No explicit llm_config:** Unlike AutoGen, CrewAI manages its own LLM configuration internally. Agents require only role, goal, backstory, and optionally tools.

**kickoff() return value:** Returns only the final task's output — the editor's polished post. Intermediate outputs (research brief, writer draft) are available post-execution via `crew.tasks[N].output` if needed.

**Role differentiation through backstory:** All three agents use the same underlying model. The behavioral differences come entirely from distinct system prompts embedded in role, goal, and backstory — demonstrating that prompt design drives agent specialization, not model differences.

## Compared to Previous Chapters

| | Ch 5 Tool Use | Ch 7 Multi-Agent |
|---|---|---|
| Agents | 1 agent + tools | 3 specialized agents |
| Collaboration | Agent ↔ tools | Agent → Agent → Agent |
| Context passing | Tool return values | Sequential task output injection |
| Specialization | Via tool descriptions | Via role/goal/backstory |
| kickoff() output | Single agent result | Final agent in pipeline |

## Running It

```bash
cd agentic-design-patterns
source .venv/bin/activate
python ch07_multi_agent_collab/main.py
```
