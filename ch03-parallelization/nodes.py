from llm import client, MODEL


def analyze_market(state):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a market analyst.  Analyze market opportunities and /"
            "competitive landscape."},
            {"role": "user", "content": f"Provide a brief market analysis for: {state['topic']}"}
        ]
    )
    return {"analyses": [f"MARKET ANALYSIS:\n{response.choices[0].message.content}"]}

def analyze_risk(state):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a risk analyst.  Identify potential risks, /"
            "challenges, and mitigation strategies."},
            {"role": "user", "content": f"Provide a brief risk analysis for: {state['topic']}"}
        ]
    )
    return {"analyses": [f"RISK ANALYSIS:\n{response.choices[0].message.content}"]}

def analyze_trends(state):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a trend analyst.  Identify emerging /"
            "trends and future directions."},
            {"role": "user", "content": f"Provide a brief trend analysis for: {state['topic']}"}
        ]
    )
    return {"analyses": [f"TREND ANALYSIS:\n{response.choices[0].message.content}"]}

def synthesize_report(state):
    combined = "\n\n".join(state.get("analyses", []))
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a senior research analyst. /"
            "Synthesize multiple analyses into a coherent executive report."},
            {"role": "user", "content": f"Synthesize these analyses into a concise executive report:\n\n{combined}"}
        ]
    )
    return {"report": response.choices[0].message.content}