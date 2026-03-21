from planner import generate_plan
from executor import execute_steps, synthesize_results


if __name__ == "__main__":
    goal = """
    Create a comprehensive onboarding guide for a new software engineer
    joining a startup, covering their first 30 days.
    """

    print(f"\n--- GOAL ---\n{goal}")

    steps = generate_plan(goal)
    results = execute_steps(steps, goal)
    final = synthesize_results(goal, results)

    print("\n--- FINAL DELIVERABLE ---")
    print(final)