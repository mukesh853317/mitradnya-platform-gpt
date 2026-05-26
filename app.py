import streamlit as st
import pandas as pd

# ====================================================
# PAGE CONFIG
# ====================================================

st.set_page_config(
    page_title="Mitradnya Learning Platform",
    layout="wide"
)

# ====================================================
# TITLE
# ====================================================

st.title("📚 Mitradnya Learning Platform 📚")

# ====================================================
# MAIN TABS
# ====================================================

main_tabs = st.tabs([
    "🎓 Student Dashboard",
    "👨‍🏫 Admin Dashboard"
])

# ====================================================
# STUDENT DASHBOARD
# ====================================================

with main_tabs[0]:

    st.header("🎓 Student Dashboard")

    student_tabs = st.tabs([
        "📖 Notes",
        "📝 Questions",
        "🎯 MCQ",
        "🎥 Study Room"
    ])

    # NOTES

    with student_tabs[0]:

        st.subheader("📖 Notes")

        uploaded_notes = st.file_uploader(
            "Upload PDF Notes",
            type=["pdf"]
        )

        if uploaded_notes:
            st.success("Notes Uploaded Successfully")

    # QUESTIONS

    with student_tabs[1]:

        st.subheader("📝 Questions")

        st.info("Questions Section Working")

    # MCQ

    with student_tabs[2]:

        st.subheader("🎯 MCQ Test")

        st.info("MCQ Section Working")

    # STUDY ROOM

    with student_tabs[3]:

        st.subheader("🎥 Study Room")

        st.info("Study Room Working")

# ====================================================
# ADMIN DASHBOARD
# ====================================================

with main_tabs[1]:

    st.header("👨‍🏫 Admin Dashboard")

    st.info("Admin Dashboard Working")
