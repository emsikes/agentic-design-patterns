# Chapter 4 — Reflection

## Pattern Overview

Reflection is an iterative self-improvement pattern where an agent generates output, a critic evaluates it, and the generator revises based on feedback. The loop continues until the critic is satisfied or a maximum iteration count is reached. Unlike prompt chaining which is linear, reflection is cyclic — the same agents interact repeatedly until a quality threshold is met.

**Core insight:** A single generation pass produces competent but unreviewed output. Adding a critic agent that provides specific, actionable feedback and a revision loop produces measurably better results — the same way human writers improve through editorial review cycles.

## Framework

**AutoGen** — First departure from LangGraph. AutoGen uses a conversation-based model rather than a graph model. Two agents exchange messages directly via `initiate_chat`. There is no graph to wire, no state object, no edges — just structured agent-to-agent conversation. This is a fundamentally different mental model: LangGraph thinks in nodes and edges, AutoGen thinks in agents and conversations.

## Our Implementation

**Mini-project:** Self-Improving Code Generator

A CodeGenerator agent writes Python code for a given task. A CodeCritic agent reviews it and either returns specific feedback or responds with `APPROVED`. The loop runs until approved or max iterations is hit.

```
task → CodeGenerator → CodeCritic → APPROVED? → yes → output final code
                            ↑_________↓ no → revise with critique → repeat
```

## File Breakdown

| File | Responsibility |
|---|---|
| `agents.py` | Defines `llm_config` and instantiates `code_generator` and `code_critic` AssistantAgents |
| `reflection_loop.py` | Controls the iteration logic — initial generation, critique loop, early exit on APPROVED |
| `main.py` | Entry point — defines the coding task and invokes the reflection loop |

## Key Concepts

**AssistantAgent:** AutoGen's LLM-backed agent. Takes a name, system message, and llm_config. Both the generator and critic are AssistantAgents — the difference is entirely in their system prompts.

**initiate_chat:** The core AutoGen method. One agent initiates a conversation with another, passing a message. `max_turns=1` limits the exchange to a single round — we control iteration manually rather than letting AutoGen loop freely.

**APPROVED keyword:** The termination signal. The critic's system prompt instructs it to respond with only "APPROVED" when satisfied. The loop checks for this string and breaks early. This is a common pattern — use an explicit sentinel word to signal completion rather than trying to parse complex LLM responses.

**last_good_code tracking:** `current_code` gets overwritten each iteration. A separate `last_good_code` variable preserves the most recently generated code so the final output isn't "APPROVED".

**llm_config structure:** AutoGen uses a `config_list` rather than a single client instance. Supports multiple model fallbacks. The `price` field silences cost warnings for models AutoGen doesn't recognize natively.

## AutoGen vs LangGraph

| | LangGraph | AutoGen |
|---|---|---|
| Mental model | Graph — nodes and edges | Conversation — agents and messages |
| State | Explicit TypedDict passed through nodes | Implicit — lives in agent message history |
| Control flow | Graph topology | Code logic around `initiate_chat` |
| Best for | Stateful pipelines, branching, parallelization | Agent-to-agent conversation, reflection, debate |

## Observed Behavior

- The critic returned the code unchanged on iteration 1 — effectively signaling approval without the keyword
- APPROVED fired on iteration 2, loop exited early
- A more complex or deliberately flawed task would produce more meaningful critique cycles
- AutoGen 0.2.x produces cosmetic warnings for unrecognized model pricing — calls succeed regardless

## Running It

```bash
cd agentic-design-patterns
source .venv/bin/activate
python ch04_reflection/main.py
```
