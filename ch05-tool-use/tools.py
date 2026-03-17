from crewai.tools import tool
from openai import OpenAI
from dotenv import load_dotenv
import os
import math


load_dotenv(override=True)
MODEL="gpt-4.1-mini"

@tool("Web Search")
def search_web(query: str) -> str:
    """Search the web for current information about a topic.
    Use this when you need up-to-date facts or recent information."""
    client = OpenAI()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a web search assistant. Return factual, concise information about the query as if you searched the web."},
            {"role": "user", "content": f"Search for: {query}"}
        ]
    )
    return response.choices[0].message.content

@tool("Calculator")
def calcualte(expression: str) -> str:
    """
    Perform mathmatical calculations.
    Use this when you need to compute numbers, percentages, or mathmatical expressions.
    Input should be a valid Python mathmatical expression.
    """
    try:
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"
    
@tool("Wikipedia Lookup")
def lookup_wikipedia(topic: str) -> str:
    """
    Look up detailed background information about a topic on Wikipedia.
    Use this when need encyclopedic, historical, or foundational knowledged.
    """
    client = OpenAI()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a Wikipedia assitant.  Return detailed, encyclopedic information /"
            "about the topic as if retrieved from Wikipedia."},
            {"role": "user", "content": f"Give me a  Wikipedia-style summary of: {topic}"}
        ]
    )
    return response.choices[0].message.content