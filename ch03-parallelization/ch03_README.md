# Chapter 3 — Parallelization

## Pattern Overview

Parallelization executes multiple nodes simultaneously rather than sequentially, then merges their results before continuing. This is the fan-out / fan-in pattern — a single entry point branches into concurrent workers, all branches must complete before the graph proceeds to the synthesis step.

**Core insight:** Sequential execution waits for each node to finish before starting the next. Parallel execution fires all branches at once and waits only as long as the slowest branch. For LLM workloads where each call has independent latency, this produces significant speedups.

## Framework

**LangGraph** — Parallelization is expressed through multiple edges leaving the same source node. LangGraph detects the fan-out pattern and executes destination nodes concurrently in a single "superstep." The join edge (`add_edge(["a", "b", "c"], "sink")`) creates a synchronization barrier — the sink node waits until all branches have completed before executing.

## Our Implementation

**Mini-project:** Research Analyst

Three specialist analyst nodes run in parallel — market, risk, and trends — each examining a different dimension of a topic. A synthesis node merges all three outputs into a final executive report.

```
invoke({"topic": "...", "analyses": []})
    → market, risk, trends   → all three run concurrently (superstep)
    → synthesize             → waits for all three, merges results, writes report
    → END
```

## File Breakdown

| File | Responsibility |
|---|---|
| `state.py` | Defines `ResearchState` with `analyses` as an `Annotated[list[str], add]` reducer field |
| `llm.py` | Shared OpenAI client and MODEL constant |
| `nodes.py` | Three parallel analyst nodes plus `synthesize_report` |
| `graph.py` | Fan-out from START, join edge for fan-in, synthesize to END |
| `main.py` | Entry point — invokes graph and prints individual analyses plus final report |

## Key Concepts

**Reducer fields:** The `analyses` field uses `Annotated[list[str], add]` to tell LangGraph how to merge results from parallel nodes. Without a reducer, last-write-wins — parallel results would overwrite each other. The reducer appends each node's list result into a single combined list.

**Superstep:** LangGraph groups parallel nodes into a single execution unit called a superstep. All nodes in the superstep run concurrently and must all complete before the graph advances. If one node fails, the entire superstep fails atomically.

**Join edge:** `graph.add_edge(["market", "risk", "trends"], "synthesize")` is a synchronization barrier. Without the list syntax, individual edges would allow `synthesize` to fire as soon as any single branch completed — before the full `analyses` list was populated.

**Field naming consistency:** Reducer fields must use the exact same name across `state.py`, all node return dicts, and `main.py` invoke. A mismatch produces a silent `KeyError` at the sink node since the correctly-named field never appears in state.

## Compared to Previous Chapters

| | Ch 1 Chaining | Ch 2 Routing | Ch 3 Parallelization |
|---|---|---|---|
| Execution | Sequential | Conditional branch | Concurrent superstep |
| Edges | `add_edge` | `add_conditional_edges` | Fan-out + join edge |
| State writes | One field per node | One handler writes `response` | Multiple nodes write same field |
| Reducer needed | No | No | Yes — `Annotated` + `add` |

## Lessons Learned

- Field names must be identical across state definition, node returns, and invoke — a single typo (e.g. `analysis` vs `analyses`) produces a KeyError at the sink node with no helpful error message
- Always initialize reducer fields in `graph.invoke()` — LangGraph does not auto-populate TypedDict fields to empty defaults
- The join edge list syntax `add_edge([...], "sink")` is required for correct fan-in — individual edges from each parallel node to the sink will cause the sink to fire prematurely

## Running It

```bash
cd agentic-design-patterns
source .venv/bin/activate
python ch03_parallelization/main.py
```
