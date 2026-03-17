from crewai import Crew, Process
from agent import researcher
from task import create_research_task


def build_crew(question: str) -> Crew:
    task = create_research_task(question)

    return Crew(
        agents=[researcher],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )