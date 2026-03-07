from graph import build_graph


graph = build_graph()

def run(query: str):
    result = graph.invoke({"query": query})

    print(f"\n--- QUERY ---")
    print(result["query"])

    print(f"\n--- INTENT ---")
    print(result["intent"])

    print(f"\n--- RESPONSE ---")
    print(result["response"])

if __name__ == "__main__":
    queries = [
        "I keep getting timeouts in my browser when trying to access google.com",
        "I was charged twice for my subscription this month",
        "What are your business hours?"
    ]

    for query in queries:
        print("\n" + "="*50)
        run(query)