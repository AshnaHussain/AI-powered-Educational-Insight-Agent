import streamlit as st
import uuid


def show_sessions():
    st.subheader("📁 Select Session")

    # Ensure sessions list exists
    if "sessions" not in st.session_state:
        st.session_state.sessions = []

    # ---------- CREATE NEW SESSION ----------
    if st.button("➕ Create New Session", key="create_new_session_btn"):
        new_session = {
            "id": str(uuid.uuid4())[:8],
            "name": f"Session {len(st.session_state.sessions) + 1}",
        }
        st.session_state.sessions.append(new_session)
        st.session_state.current_session = new_session
        st.rerun()

    st.divider()

    # ---------- SHOW EXISTING SESSIONS ----------
    if not st.session_state.sessions:
        st.info("No sessions available. Please create one.")
        return

    for idx, session in enumerate(st.session_state.sessions):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f"📂 **{session['name']}**")

        with col2:
            if st.button(
                "Open",
                key=f"open_session_{session['id']}",
            ):
                st.session_state.current_session = session
                st.rerun()
