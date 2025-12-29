import streamlit as st
import matplotlib.pyplot as plt

def show_average_score(df):
    avg = df["Marks"].mean()
    st.metric("Average Score", f"{avg:.2f}")

def show_subject_wise_chart(df):
    fig, ax = plt.subplots()
    ax.bar(df["Subject"], df["Marks"])
    ax.set_xlabel("Subject")
    ax.set_ylabel("Marks")
    ax.set_title("Subject-wise Performance")
    plt.xticks(rotation=45)
    st.pyplot(fig)
