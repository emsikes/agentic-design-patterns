from langgraph.graph import StateGraph, END

from state import TicketState
from classifier import classify_intent
from nodes import handle_technical, handle_billing, handle_general


def route_intent(state):
    intent = state["intent"]
    if intent == "technical":
        return "technical"
    elif intent == "billing":
        return "billing"
    else:
        return "general"
    
def build_graph():
    graph = StateGraph(TicketState)

    graph.add_node("classify", classify_intent)
    graph.add_node("technical", handle_technical)
    graph.add_node("billing", handle_billing)
    graph.add_node("general", handle_general)

    graph.set_entry_point("classify")

    graph.add_conditional_edges(
        "classify",
        route_intent,
        {
            "technical": "technical",
            "billing": "billing",
            "general": "general"
        }
    )

    graph.add_edge("technical", END)
    graph.add_edge("billing", END)
    graph.add_edge("general", END)

    return graph.compile()