import streamlit as st
import pandas as pd

# ---------------- COMPONENTS ----------------
from components.login import show_login
from components.sessions import show_sessions
from components.analysis_form import show_analysis_form
from components.chat_ui import show_chat

# ---------------- SERVICES ----------------
from services.ai_service import generate_analysis

# ---------------- UTILS ----------------
from utils.charts import show_average_score, show_subject_wise_chart
from config.prompts import AGENT_PROMPTS


# ---------------- SESSION STATE INIT ----------------
def init_session_state():
    defaults = {
        "user": None,
        "current_session": None,
        "sessions": [],
        "analysis_result": None,
        "report_df": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# ---------------- MAIN APP ----------------
def main():
    st.set_page_config(
        page_title="EIA – Education Insights Agent",
        layout="wide"
    )

    init_session_state()

    # ---------- LOGIN ----------
    if st.session_state.user is None:
        show_login()
        return

    # ---------- SESSION ----------
    if st.session_state.current_session is None:
        show_sessions()
        return

    # ---------- MAIN UI ----------
    st.title("📊 Student Report Analysis")

    # Upload / extract CSV → returns DataFrame
    extracted_data = show_analysis_form()

    # ---------- PROCESS DATA ----------
    if isinstance(extracted_data, pd.DataFrame) and not extracted_data.empty:
        df = extracted_data.copy()
        st.session_state.report_df = df

        try:
            # ---------- AI ANALYSIS ----------
            results = []
            for prompt in AGENT_PROMPTS.values():
                response = generate_analysis(
                    data=df.to_dict(orient="records"),
                    system_prompt=prompt
                )

                # Normalize response
                if isinstance(response, dict):
                    results.append(response.get("content", str(response)))
                else:
                    results.append(str(response))

            st.session_state.analysis_result = "\n\n".join(results)

        except Exception as e:
            st.error(f"AI processing error: {e}")
            return

    # ---------- SHOW AI INSIGHTS ----------
    if isinstance(st.session_state.analysis_result, str) and st.session_state.analysis_result.strip():
        st.subheader("🧠 AI Academic Insights")
        st.write(st.session_state.analysis_result)

    # ---------- CHARTS ----------
    if isinstance(st.session_state.report_df, pd.DataFrame) and not st.session_state.report_df.empty:
        st.subheader("📈 Visual Academic Insights")

        show_average_score(st.session_state.report_df)
        show_subject_wise_chart(st.session_state.report_df)

    # ---------- CHAT ----------
    if (
        isinstance(st.session_state.analysis_result, str)
        and st.session_state.analysis_result.strip()
        and isinstance(st.session_state.report_df, pd.DataFrame)
    ):
        st.subheader("💬 Ask AI (Follow-up)")

        show_chat(
            context_text=st.session_state.analysis_result,
            report_df=st.session_state.report_df
        )


if __name__ == "__main__":
    main()
