import streamlit as st
import pandas as pd

def show_analysis_form():
    st.subheader("📄 Upload Student Marksheet")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file is None:
        return None

    df = pd.read_csv(uploaded_file)

    st.success("File processed successfully")
    st.dataframe(df)

    return df
