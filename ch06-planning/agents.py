from autogen import AssistantAgent
from dotenv import load_dotenv
import os


load_dotenv(override=True)

llm_config = {
    "config_list": [
        {
            "model": "gpt-4.1-mini",
            "api_key": os.getenv("OPENAI_API_KEY"),
            "price": [0.004, 0.0016]
        }
    ]
}

planner = AssistantAgent(
    name="Planner",
    system_message="""You are a strategic planner.  When given a goal, break it down /
    into a numbered list of clear, concrete, executable steps. /
    Return ONLY the numbered steps, no additional comentary. /
    Each step should be self-contained and actionable.""",
    llm_config=llm_config
)

executor = AssistantAgent(
    name="Exector",
    system_message="""You are an expert executor.  When given a single task step, /
    carry it out thoroughly and return the results. /
    Be specific, detailed, and actionable in your output.""",
    llm_config=llm_config
)

synthesizer = AssistantAgent(
    name="Synthesizer",
    system_message="""You are an expert at synthesizing informaiton. /
    Given a goal and a set of completed step results, combine them into /
    a cohesive, well-structured final deliverable that fully achieves the goal.""",
    llm_config=llm_config
)