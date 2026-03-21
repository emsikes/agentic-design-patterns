from agents import planner
import re


def generate_plan(goal: str) -> list[str]:
    planner.initiate_chat(
        planner,
        message=f"Create a step-by-step plan to accomplish this goal: {goal}",
        max_turns=1
    )

    response = planner.last_message()["content"]

    # Parse the list of numbered steps from the response
    steps = re.findall(r'\d+\.\s+(.+?)(?=\n\d+\.|\Z)', response, re.DOTALL)
    steps = [step.strip() for step in steps]

    print(f"\n--- PLAN ({len(steps)} steps) ---")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

    return steps