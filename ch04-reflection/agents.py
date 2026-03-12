from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
import os

load_dotenv(override=True)

llm_config = {
    "config_list": [
        {
            "model": "gpt-4.1-mini",
            "api_key": os.getenv("OPENAI_API_KEY"),
            "price": [0.0004, 0.0016]
        }
    ]
}

code_generator = AssistantAgent(
    name="CodeGenerator",
    system_message = """You are an expert Python developer.  
When given a coding task, write clean, well-commented Python code.  
When given a critique, revise your code to address the feedback.  
Always return the complete revised code, not just the changes."""
)

code_critic = AssistantAgent(
    name="CodeCritic",
    system_message="""You are a senior code reviewer.
Evaluate Python code for correctness, effeciency, readability, and best practices.
If the code is satisfactory, respond with only the word APPROVED.
If improvements are needed, provide specific, actionable feedback.
Be concise and direct.""",
    llm_config=llm_config
)