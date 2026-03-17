from crewai import Agent
from tools import search_web, calcualte, lookup_wikipedia


researcher = Agent(
    role="Research Assistant",
    goal="Answer research questions accurately using the available tools",
    backstory="""You are an expert research assistant with access to the web search,
    a calculator, and Wikipedia.  You always use the most appropriate tool for
    each part of a research question and sythesize findings into clear answers.""",
    tools=[search_web, calcualte, lookup_wikipedia],
    verbose=True
)