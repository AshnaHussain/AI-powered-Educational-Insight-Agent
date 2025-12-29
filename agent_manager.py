from services.ai_service import get_chat_response
from config.prompts import AGENT_PROMPTS
import streamlit as st

def run_agents(report_text):
    agent_outputs = {}

    for agent_name, prompt in AGENT_PROMPTS.items():
        st.write(f"🔹 Running {agent_name}...")

        response = get_chat_response(
            f"""
{prompt}

Here is the student's marksheet data:
{report_text}
""",
            "",
            []
        )

        agent_outputs[agent_name] = response

    return agent_outputs
