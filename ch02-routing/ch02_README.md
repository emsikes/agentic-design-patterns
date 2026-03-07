# Chapter 2 — Routing

## Pattern Overview

Routing inspects the content of an input and dynamically decides which node to execute next. Rather than a fixed linear sequence, the graph branches based on a classification decision. This enables a single entry point to dispatch to specialized handlers — each optimized for a specific intent, domain, or task type.

**Core insight:** A single generalist prompt handles all query types poorly. Routing lets you apply the right specialist — with the right system prompt and persona — to each class of input. The routing decision and the response logic are always kept in separate nodes.

## Framework

**LangGraph** — Routing maps directly to `add_conditional_edges`. After the classifier node runs, LangGraph calls a routing function that reads state and returns a node name. The graph uses that return value to determine the next node to execute. All other paths are simply never called.

## Our Implementation

**Mini-project:** Support Ticket Router

A classifier node determines the intent of an incoming support query, then the graph routes to one of three specialist handler nodes.

```
invoke({"query": "..."})
    → classify_intent    → populates state["intent"]
    → route_intent()     → reads intent, returns node name
    → handle_technical   → (if intent == "technical")
    → handle_billing     → (if intent == "billing")
    → handle_general     → (if intent == "general")
    → END
```

## File Breakdown

| File | Responsibility |
|---|---|
| `state.py` | Defines `TicketState` TypedDict — query, intent, response |
| `llm.py` | Shared OpenAI client and MODEL constant |
| `classifier.py` | Single node that classifies query into one of three intents |
| `nodes.py` | Three specialist handler nodes — one per intent |
| `graph.py` | Wires classifier, routing function, and handlers via `add_conditional_edges` |
| `main.py` | Entry point — runs three queries to exercise all three routes |

## Key Observations

- `intent` is a **control field** — it carries no output value for the user, it exists purely to drive the routing decision
- The classifier system prompt explicitly enumerates valid categories and constrains output to a single word — vague classifier prompts produce inconsistent routing
- `.strip().lower()` defensively normalizes classifier output — never trust raw LLM output as a routing key
- Only one handler node executes per invocation — unlike Ch 1 where every node ran
- All three handlers write to the same `response` field — only one will ever populate it per run
- Handler nodes have no awareness of how they were reached — routing logic and response logic are fully decoupled
- The `else` branch in `route_intent` acts as a defensive default — unexpected classifier output falls through to `general`
- `add_conditional_edges` takes three arguments: source node, routing function, and a dict mapping return values to node names

## Compared to Chapter 1

| | Ch 1 Prompt Chaining | Ch 2 Routing |
|---|---|---|
| Edge type | `add_edge` (fixed) | `add_conditional_edges` (dynamic) |
| Nodes executed | All nodes, every run | Only the classified path |
| State fields | All fields populated | Only the matched handler populates `response` |
| Control flow | Sequential | Branching |

## Running It

```bash
cd agentic-design-patterns
source .venv/bin/activate
python ch02_routing/main.py
```
