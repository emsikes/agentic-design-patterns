from crewai import Task
from agents import researcher, writer, editor


def create_tasks(topic: str):
    research_task = Task(
        description=f"""Research the following topic thoroughly: {topic}

        Produce a comprehensive research brief covering:
        - Key concepts and definitions
        - Current state and recent developments
        - Important trends and future directions
        - Notable examples or case studies
        - Key challenges open questions.""",
        expected_output="""A well-organized research brief with clearly labeled /
        sections covering all the requested areas.  Use bullet points and headers for clarity.""",
        agent=researcher
    )

    write_task = Task(
        description="""Using the research brief provided, write an engaging /
        technical blog post that:
        - Has a compelling introduction that hooks the reader
        - Covers all key points from the research brief
        - Uses concrete examples and analogies where helpful
        = Is structured with clear headings and secions
        - Ends with a strong conclusion and key takeaways""",
        expected_output="""A complete technical blog post of 600-800 words, /
        well-structured with headings, ready for editorial review.""",
        agent=writer
    )

    edit_task = Task(
        description="""Review and polish the blog post draft provided:
        - Fix any gramatical or structure issues
        - Improve clarity and readability
        - Ensure consistent tone throughout
        - Strengthen the introduction and conculsion
        - Verify technical accuracy of all claims
        - Return the complete polished post.""",
        expected_output="""A publication-ready technical blog post with all issues addressed. /
        Return the complete revised post.""",
        agent=editor
    )

    return [research_task, write_task, edit_task]