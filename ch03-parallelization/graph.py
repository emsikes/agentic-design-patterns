from langgraph.graph import StateGraph, START, END

from state import ResearchState
from nodes import analyze_market, analyze_risk, analyze_trends, synthesize_report


def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("market", analyze_market)
    graph.add_node("risk", analyze_risk)
    graph.add_node("trends", analyze_trends)
    graph.add_node("synthesize", synthesize_report)

    # Fan-out from START
    graph.add_edge(START, "market")
    graph.add_edge(START, "risk")
    graph.add_edge(START, "trends")

    # Join edge — synthesize waits for ALL three to complete
    graph.add_edge(["market", "risk", "trends"], "synthesize")

    graph.add_edge("synthesize", END)

    return graph.compile()