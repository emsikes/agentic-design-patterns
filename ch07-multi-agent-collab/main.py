from crew import build_crew


if __name__ == "__main__":
    topic = "The rise of agentic AI systems and their impact on software development"

    print(f"\n--- TOPIC --\n{topic}")

    crew = build_crew(topic)
    result = crew.kickoff()

    print("\n--- FINAL BLOG POST ---")
    print(result)