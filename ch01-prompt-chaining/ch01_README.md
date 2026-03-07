# Chapter 1 — Prompt Chaining

## Pattern Overview

Prompt chaining decomposes a complex task into a sequence of focused LLM calls where each call's output becomes the next call's input. Rather than asking a single prompt to do everything, each node in the chain has one responsibility — producing more reliable, higher quality results at every stage.

**Core insight:** A single prompt asking for a "great blog post" produces competent but generic output. Decomposing into outline → draft → critique → refine produces meaningfully better results at each stage because each LLM call is scoped to one task.

## Framework

**LangGraph** — The linear chain maps directly to LangGraph's node/edge model. Each node is a Python function registered on a `StateGraph`. Edges define the fixed execution order. The state object accumulates fields as it passes through each node.

## Our Implementation

**Mini-project:** Blog Post Pipeline

A 4-node pipeline that takes a topic string and produces a fully drafted and refined blog post.

```
invoke({"topic": "..."})
    → generate_outline   → populates state["outline"]
    → generate_draft     → populates state["draft"]
    → critique_draft     → populates state["critique"]
    → refine_draft       → populates state["final"]
```

## File Breakdown

| File | Responsibility |
|---|---|
| `state.py` | Defines `BlogState` TypedDict — the shape of data flowing through the graph |
| `llm.py` | Shared OpenAI client instance, loaded from `.env` |
| `nodes.py` | Four node functions — each reads from state and returns one new field |
| `graph.py` | Wires nodes and edges, compiles the runnable graph via `build_graph()` |
| `main.py` | Entry point — invokes the graph with a topic and prints all pipeline stages |

## Key Observations

- Each node owns exactly one input field and one output field — scoped, single-responsibility LLM calls
- Any node can read any previously populated state field — `refine_draft` reads both `draft` and `critique`
- The model has no awareness it is part of a chain — LangGraph manages state, not the model
- `compile()` validates the graph structure before execution — catches wiring errors early
- `add_edge` defines a strictly linear flow — no branching (that comes in Ch 2)

## Running It

```bash
cd agentic-design-patterns
source .venv/bin/activate
python ch01_prompt_chaining/main.py
```
