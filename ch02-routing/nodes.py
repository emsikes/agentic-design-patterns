from llm import client, MODEL


def handle_technical(state):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a technical support specialist.  \
             Provide clear, step-by-step toubleshooting guidance."},
             {"role": "user", "content": state["query"]}
        ]
    )
    return {"response": response.choices[0].message.content}

def handle_billing(state):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a billing support specialist.  \
             Be empathetic, clear, and precise about account and payment related issues."},
             {"role": "user", "content": state["query"]}
        ]
    )
    return {"response": response.choices[0].message.content}

def handle_general(state):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a friendly and helpful general support assistant.  \
             Answer questions clearly and concisely."}
        ]
    )
    return {"response": response.choices[0].message.content}