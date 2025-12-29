import streamlit as st
from services.ai_service import generate_analysis

def show_chat(context_text, report_df):
    question = st.text_input("Ask a question about the student's performance:")

    if st.button("Ask"):
        if question.strip() == "":
            st.warning("Please type a question")
            return

        prompt = f"""
You are an academic advisor.

Context:
{context_text}

Student Data:
{report_df.to_string(index=False)}

Question:
{question}
"""

        answer = generate_analysis(
            data=prompt,
            system_prompt="Answer clearly using student marks."
        )

        # Check if the request was successful
        if answer.get('success'):
            # Get the content and format it properly
            content = answer['content']
            
            # Display with proper formatting using markdown
            st.markdown(content)
        else:
            # Show error if request failed
            st.error(f"Error: {answer.get('error', 'Unknown error')}")