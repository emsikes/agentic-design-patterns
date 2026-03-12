from reflection_loop import run_reflection_loop


if __name__ == "__main__":
    task = """
    Write a Python function that:
    1. Takes a list of dictionaries containing 'name' and 'score' keys
    2. Returns the top 3 performers sorted by score in descending order
    3. Handles edge cases like empty lists and missing keys  
    """

    run_reflection_loop(task, max_iterations=3)