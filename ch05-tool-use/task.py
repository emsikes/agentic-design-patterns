from crewai import Task
from agent import researcher


def create_research_task(question: str) -> Task:
    return Task(
        description=f"""Research the following questions thoroughly: {question}
        Use the available tools to gather information.
        Use the calculator if any numerical analysis is needed.
        Synthesize all findings into a comprehensive answer.""",
        expected_output="""A well-strucured research summary that directly answers
        the question with supporting facts and any relevant calculations.""",
        agent=researcher
    )