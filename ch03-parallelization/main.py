from graph import build_graph

graph = build_graph()


def run(topic: str):
    result = graph.invoke({"topic": topic, "analyses": []})

    print("\n--- INDIVIDUAL ANALYSES ---")
    for analysis in result["analyses"]:
        print(f"\n{analysis}")
        print("-" * 40)

    print("\n--- FINAL REPORT ---")
    print(result["report"])

if __name__ == "__main__":
    run("AI Agents in Healthcare")