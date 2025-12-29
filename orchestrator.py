from services.ai_service import get_chat_response
from config.prompts import AGENT_PROMPTS

def orchestrate(agent_outputs):
    combined_input = ""

    for agent, output in agent_outputs.items():
        combined_input += f"\n\n{agent.upper()} OUTPUT:\n{output}"

    final_response = get_chat_response(
        f"""
{AGENT_PROMPTS["orchestrator_agent"]}

Below are the outputs from specialized agents:
{combined_input}
""",
        "",
        []
    )

    return final_response
