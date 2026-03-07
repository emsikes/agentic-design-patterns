from typing import TypedDict


class TicketState(TypedDict):
    query: str
    intent: str
    response: str