from services.ai_service import get_chat_response
from config.prompts import CHAT_AGENT_PROMPT


def get_followup_response(user_question, report_text, ai_insights):
    """
    Generates a context-aware follow-up response using:
    - Student report text
    - AI-generated academic insights
    - User's follow-up question
    """

    prompt = f"""
{CHAT_AGENT_PROMPT}

STUDENT REPORT:
{report_text}

AI INSIGHTS:
{ai_insights}

USER QUESTION:
{user_question}
"""

    response = get_chat_response(
        prompt,
        "",
        []
    )

    return response
