from crewai import Crew, Process
from agents import researcher, writer, editor
from tasks import create_tasks


def build_crew(topic: str) -> Crew:
    tasks = create_tasks(topic)

    return Crew(
        agents=[researcher, writer, editor],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )