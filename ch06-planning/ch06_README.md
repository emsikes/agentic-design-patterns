# Chapter 6 — Planning

## Pattern Overview

Planning separates thinking from doing. Rather than asking an agent to accomplish a complex goal in one pass, the planning pattern first decomposes the goal into explicit, ordered steps, then executes each step independently, then synthesizes all results into a final deliverable. This produces more reliable, comprehensive outputs on complex tasks than any single prompt could achieve.

**Core insight:** A single prompt asked to "create a 30-day onboarding guide" produces a generic outline. A planner that decomposes the goal into 12 concrete steps, executes each thoroughly, and synthesizes the results produces a genuinely detailed and actionable document. Planning is about breadth — breaking a problem apart before solving it.

**Planning vs Reflection (Ch 4):**
- Reflection loops on a single output until quality improves — depth on one artifact
- Planning decomposes a goal into sub-tasks and executes them in sequence — breadth across many artifacts
- They are complementary — a planning agent could use reflection on each step

## Framework

**AutoGen** — Two-agent conversation model. The Planner, Executor, and Synthesizer are all `AssistantAgent` instances differentiated only by their system prompts. Execution is controlled manually in Python rather than through graph topology. `initiate_chat` with `max_turns=1` is used for each interaction — we own the loop.

## Our Implementation

**Mini-project:** Task Decomposition Agent

A three-agent pipeline decomposes a complex goal into steps, executes each step independently, then synthesizes all outputs into a final deliverable.

```
goal → Planner → [step 1...N] → Executor (×N, stateless) → Synthesizer → final output
```

**Task used:** Create a comprehensive 30-day onboarding guide for a new software engineer joining a startup.

**Result:** 12-step plan fully executed and synthesized into a structured onboarding document with milestones table, weekly timeline, coding tasks, communication guidelines, and support contacts.

## File Breakdown

| File | Responsibility |
|---|---|
| `agents.py` | Defines `llm_config` and three `AssistantAgent` instances — planner, executor, synthesizer |
| `planner.py` | `generate_plan()` — prompts the planner and parses numbered steps via regex |
| `executor.py` | `execute_steps()` — iterates steps and calls executor for each; `synthesize_results()` — calls synthesizer with all outputs |
| `main.py` | Entry point — defines goal, calls plan → execute → synthesize in sequence |

## Key Concepts

**Stateless executor:** The Executor receives one step at a time with no knowledge of the broader plan or other steps. This keeps each execution focused and prevents the model from making assumptions about context it wasn't given. Only the Synthesizer sees the full picture.

**Format-constrained planning:** The Planner's system prompt enforces a numbered list format — "Return ONLY the numbered steps." This is essential because the output is parsed programmatically. Format constraints in system prompts exist to make downstream parsing predictable and reliable.

**Regex step parsing:** `re.findall(r'\d+\.\s+(.+?)(?=\n\d+\.|\Z)', response, re.DOTALL)` extracts step text between numbered items. The non-greedy `?` combined with a lookahead prevents one match from consuming multiple steps. `\Z` handles the final step which has no following number to stop at.

**Manual loop control:** Unlike AutoGen's built-in conversation loops, we control iteration explicitly in Python — generate plan, loop over steps, call executor per step, then synthesize. `max_turns=1` on every `initiate_chat` keeps each exchange to a single round.

## Observed Behavior

- Planner generated 12 steps for a 30-day onboarding guide goal — more than typical, reflecting genuine task complexity
- Each executor step produced detailed, independent output with no knowledge of other steps
- Synthesizer produced a coherent, well-structured document — not a concatenation but a genuine synthesis
- Final output included tables, weekly timelines, coding task matrices, and support contact templates

## Compared to Previous Chapters

| | Ch 4 Reflection | Ch 6 Planning |
|---|---|---|
| Pattern type | Depth — iterative improvement | Breadth — goal decomposition |
| Number of LLM calls | Variable (loop until approved) | Fixed (1 plan + N steps + 1 synthesis) |
| Agent awareness | Critic sees full draft | Executor sees only one step |
| Termination | APPROVED signal | All steps executed |

## Running It

```bash
cd agentic-design-patterns
source .venv/bin/activate
python ch06_planning/main.py
```
