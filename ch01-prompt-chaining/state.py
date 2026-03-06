from typing import TypedDict


class BlogState(TypedDict):
    topic: str
    outline: str
    draft: str
    critique: str
    final: str