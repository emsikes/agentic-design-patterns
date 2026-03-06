from langgraph.graph import StateGraph, END
from state import BlogState
from nodes import generate_outline, generate_draft, critique_draft, refine_draft


def build_graph():
    graph = StateGraph(BlogState)

    graph.add_node("outline", generate_outline)
    graph.add_node("draft", generate_draft)
    graph.add_node("critique", critique_draft)
    graph.add_node("refine", refine_draft)

    graph.set_entry_point("outline")

    graph.add_edge("outline", "draft")
    graph.add_edge("draft", "critique")
    graph.add_edge("critique", "refine")
    graph.add_edge("refine", END)

    return graph.compile()