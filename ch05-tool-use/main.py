from crew import build_crew


if __name__ == "__main__":
    question = """
    What is the current state of quantum computing, and if a quantum computer
    can perform 1 million operations per second while a classical computer
    performs 1 billion, what percentage faster is the quantum computer?
    """

    crew = build_crew(question)
    result = crew.kickoff()

    print("\n--- FINAL ANSWER ---")
    print(result)