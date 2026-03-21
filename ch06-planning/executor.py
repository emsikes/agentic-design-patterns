from agents import executor, synthesizer


def execute_steps(steps: list[str], goal: str) -> list[str]:
    results = []

    for i, step in enumerate(steps, 1):
        print(f"\n--- EXECUTING STEP {i} ---")

        executor.initiate_chat(
            executor,
            message=f"Execute this task step thoroughly: {step}",
            max_turns=1
        )

        result = executor.last_message()["content"]
        results.append(f"Step {i} - {step}:\n{result}")
        print(f"Step {i} completed.")

    return results

def synthesize_results(goal: str, results: list[str]) -> str:
    combined = "\n\n".join(results)

    synthesizer.initiate_chat(
        synthesizer,
        message=f"""Goal: {goal}

Completed step results:
{combined}

Synthesize these results into a cohesive final deliverale.""",
    max_turns=1
    )

    return synthesizer.last_message()["content"]