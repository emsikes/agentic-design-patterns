from llm import client, MODEL


def classify_intent(state):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": """You are an intent classifier for a support system.
Classify the user query into exactly one of these categories:
- technical
- billing
- general
            
Respond with only the category word.  No punctuation, no explanation."""},
        {"role": "user", "content": state["query"]}
        ]
    )
    intent = response.choices[0].message.content.strip().lower()
    return {"intent": intent}