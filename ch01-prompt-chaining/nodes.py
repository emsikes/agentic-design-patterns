from llm import client


def generate_outline(state):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are an expert blog planner."},
            {"role": "user", "content": f"Create a structured outline for a blog post about: {state['topic']}"}
        ]
    )
    return {"outline": response.choices[0].message.content}

def generate_draft(state):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are an expert blog post writeer."},
            {"role": "user", "content": f"Write a full blog post draft based on this outline:\n\n{state['outline']}"}
        ]
    )
    return {"draft": response.choices[0].message.content}

def critique_draft(state):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a sharp editorial critic.  Be constructive but direct."},
            {"role": "user", 
             "content": f"Critique this blog post draft and identify specific improvements.  \
                            Also remove any double dahses and other wording or phrasing that are \
                            common to LLM generated output:\n\n{state['draft']}"}
        ]
    )
    return {"critique": response.choices[0].message.content}

def refine_draft(state):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are an expert editor who improves writing based on feedback."},
            {"role": "user", 
             "content": f"Rewrite this blog post draft incorporating the critique below:\
                            \n\nDraft:\n{state['draft']}\n\nCritique:\n{state['critique']}"}
        ]
    )
    return {"final": response.choices[0].message.content}