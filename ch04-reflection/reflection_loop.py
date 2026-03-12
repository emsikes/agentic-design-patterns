from agents import code_generator, code_critic


def run_reflection_loop(task: str, max_iterations: int = 3):
    print(f"\n--- TASK ---\n{task}")

    # Initial code generation
    code_generator.initiate_chat(
        code_critic,
        message=task,
        max_turns=1
    )

    current_code = code_generator.last_message()["content"]

    last_good_code = current_code

    for i in range(max_iterations):
        # Iterate until the last code_critic message is "APPROVED"
        critique = code_critic.last_message()["content"]
        
        print(f"\n--- ITERATION {i+1} CRITIQUE ---\n{critique}")
        
        if "APPROVED" in critique:
            print(f"\n--- CODE APPROVED AFTER {i+1} ITERATION(S) ---")
            break
        
        last_good_code = critique  # critic returns code when not APPROVED
        
        code_generator.initiate_chat(
            code_critic,
            message=f"Revise your code based on this critique:\n\n{critique}\n\nOriginal code:\n{current_code}",
            max_turns=1
        )
        
        current_code = code_generator.last_message()["content"]
    
    print(f"\n--- FINAL CODE ---\n{last_good_code}")
    return last_good_code