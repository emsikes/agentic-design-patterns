from graph import build_graph


graph = build_graph()

def run(topic: str):
    result = graph.invoke({"topic": topic})

    print("\n--- OUTLINE ---")
    print(result["outline"])
    
    print("\n--- DRAFT ---")
    print(result["draft"])

    print("\n--- CRITIQUE ---")
    print(result["critique"])

    print("\n--- FINAL OUTPUT ---")
    print(result["final"])

if __name__ == "__main__":
    run("The Future of AI Agents in Healthcare")