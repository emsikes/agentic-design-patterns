from typing import TypedDict, Annotated
from operator import add


class ResearchState(TypedDict):
    """
    Annotated with 'add' as the reducer.  In LangChain when parallel modes each return {"analyses"}: [...],
    LangGraph will merge the lists via add() instead of overwriting.  By default, the last write wins,
    which would cause the parallel execution results to be lost.
    """
    topic: str
    analyses: Annotated[list[str], add]
    report: str