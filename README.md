# Agentic Design Patterns — Hands-On Mini Projects

A chapter-by-chapter implementation series based on **Agentic Design Patterns** by Antonio Gulli. Each chapter is paired with a focused mini-project that demonstrates the core pattern in working code.

## Goals

- Build deep intuition for each agentic design pattern through hands-on implementation
- Rotate across the top production agentic frameworks to understand their strengths and tradeoffs
- Standardize on the **chat completions API** regardless of framework or model provider
- Implement function by function — understanding every component before moving forward

---

## Framework Rotation

| Framework | Strengths Covered |
|---|---|
| **LangGraph** | Stateful graphs, prompt chaining, routing, memory, HITL |
| **CrewAI** | Multi-agent collaboration, role-based patterns, tool use |
| **AutoGen** | Reflection, planning, reasoning, conversational agents |
| **OpenAI Agents SDK** | MCP, RAG, guardrails, resource optimization |

All projects use the **OpenAI chat completions API** as the standard LLM interface.

---

## Project Structure

```
agentic-design-patterns/
├── .env                          # Shared API keys (not committed)
├── .venv/                        # Single shared virtual environment
├── requirements.txt
├── README.md
│
├── ch01_prompt_chaining/         # LangGraph
├── ch02_routing/                 # LangGraph
├── ch03_parallelization/         # LangGraph
├── ch04_reflection/              # AutoGen
├── ch05_tool_use/                # CrewAI
├── ch06_planning/                # AutoGen
├── ch07_multi_agent_collab/      # CrewAI
├── ch08_memory_management/       # LangGraph
├── ch09_learning_adaptation/     # AutoGen
├── ch10_mcp/                     # OpenAI Agents SDK
├── ch11_goal_setting/            # AutoGen
├── ch12_exception_handling/      # LangGraph
├── ch13_human_in_the_loop/       # LangGraph
├── ch14_rag/                     # OpenAI Agents SDK
├── ch15_inter_agent_comms/       # CrewAI
├── ch16_resource_optimization/   # OpenAI Agents SDK
├── ch17_reasoning/               # AutoGen
├── ch18_guardrails/              # OpenAI Agents SDK
├── ch19_evaluation/              # CrewAI
└── ch20_prioritization/          # CrewAI
```

---

## Environment Setup

**Python:** 3.11.9 (via pyenv)

```bash
git clone <repo-url>
cd agentic-design-patterns
pyenv local 3.11.9
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
```

```
OPENAI_API_KEY=your-key-here
```

---

## Chapter Index

### Part I — The Patterns

| # | Pattern | Framework | Mini-Project |
|---|---|---|---|
| 1 | Prompt Chaining | LangGraph | Blog post pipeline: topic → outline → draft → critique → final |
| 2 | Routing | LangGraph | Intent router: classify input and dispatch to specialist nodes |
| 3 | Parallelization | LangGraph | Multi-branch research: parallel topic analysis with result synthesis |
| 4 | Reflection | AutoGen | Self-improving code generator with iterative critique loop |
| 5 | Tool Use / Function Calling | CrewAI | Research agent with web search, calculator, and file tools |
| 6 | Planning | AutoGen | Task decomposition agent that builds and executes a step plan |
| 7 | Multi-Agent Collaboration | CrewAI | Three-agent content team: researcher, writer, editor |
| 8 | Memory Management | LangGraph | Stateful assistant with short-term and long-term memory |
| 9 | Learning and Adaptation | AutoGen | Self-improving coding agent (SICA) with feedback loop |
| 10 | Model Context Protocol (MCP) | OpenAI Agents SDK | MCP tool server with ADK agent consumer |
| 11 | Goal Setting and Monitoring | AutoGen | Goal-driven agent with progress tracking and replanning |
| 12 | Exception Handling and Recovery | LangGraph | Resilient pipeline with retry logic and fallback nodes |
| 13 | Human-in-the-Loop | LangGraph | Approval gate agent that pauses for human review |
| 14 | Knowledge Retrieval (RAG) | OpenAI Agents SDK | Document Q&A agent with vector retrieval |
| 15 | Inter-Agent Communication (A2A) | CrewAI | Agent-to-agent handoff with structured message passing |
| 16 | Resource-Aware Optimization | OpenAI Agents SDK | Cost-aware router that selects models by task complexity |
| 17 | Reasoning Techniques | AutoGen | Chain-of-thought and ReAct reasoning agent |
| 18 | Guardrails / Safety Patterns | OpenAI Agents SDK | Input/output safety layer with policy enforcement |
| 19 | Evaluation and Monitoring | CrewAI | LLM-as-judge eval harness with scoring and logging |
| 20 | Prioritization | CrewAI | Task prioritization agent with dynamic queue management |

### Part II — The Supplement

| # | Chapter | Approach |
|---|---|---|
| 21 | Exploration and Discovery | Pure Python + chat completions |
| 22 | Advanced Prompting Techniques | Pure Python + chat completions |
| 23 | AI Agentic Interactions | LangGraph |
| 24 | Overview of Agentic Frameworks | Comparative code exercise |
| 25 | Building an Agent with AgentSpace | Google ADK |

---

## Key Design Decisions

**Single venv:** All chapters share one virtual environment at the project root. The frameworks (LangGraph, CrewAI, AutoGen, OpenAI Agents SDK) share pydantic v2 and httpx as common dependencies with no known conflicts on Python 3.11.

**Chat completions standard:** Every mini-project calls the chat completions endpoint directly, regardless of the framework in use. This keeps the focus on the agentic pattern rather than provider-specific SDKs and makes projects portable across model providers.

**Function-by-function implementation:** Each project is built incrementally — one function at a time — to ensure deep understanding of every component before moving forward.

---

## Reference

- **Book:** Agentic Design Patterns by Antonio Gulli
- **Python:** 3.11.9
- **Primary LLM:** OpenAI GPT-4o-mini (chat completions API)
