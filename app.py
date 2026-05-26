import streamlit as st
import pandas as pd
import google.generativeai as genai
API_KEY = "AIzaSyAN8CnJurB961hY-S9PWbyfuNBI0uVlrGI"

genai.configure(api_key=API_KEY)

st.set_page_config(
    page_title="Mitradnya Learning Platform",
    layout="wide"
)

st.title("📚 Mitradnya Learning Platform")

main_tabs = st.tabs([
    "🎓 Student Dashboard",
    "👨‍🏫 Admin Dashboard"
])

# ====================================================
# STUDENT
# ====================================================

with main_tabs[0]:

    st.header("🎓 Student Dashboard")

    student_tabs = st.tabs([
        "📖 Notes",
        "📝 Questions",
        "🎯 MCQ",
        "📄 Board Papers",
        "🎥 Study Room"
    ])

    # NOTES

    with student_tabs[0]:

        st.subheader("📖 Notes")

        uploaded_notes = st.file_uploader(
            "Upload Notes",
            type=["pdf"]
        )

        if uploaded_notes:

            st.success("Notes Uploaded")

    # QUESTIONS

    with student_tabs[1]:

        st.subheader("📝 Questions")

        question = st.selectbox(
            "Select Question",
            [
                "Partnership Final Account",
                "NPO",
                "Bills of Exchange"
            ]
        )

        st.info(question)

if st.button("Show Solution"):

    with st.spinner("Generating Solution..."):

        try:

            model = genai.GenerativeModel(
                "gemini-1.5-flash"
            )

            prompt = f"""
            Solve this Maharashtra Board question step-by-step.

            Use:
            - proper format
            - easy explanation
            - board pattern

            Question:
            {question}
            """

            response = model.generate_content(
                prompt
            )

            st.write(response.text)

        except Exception as e:

            st.error(e)

    # MCQ

    with student_tabs[2]:

        st.subheader("🎯 MCQ Test")

        answer = st.radio(
            "Capital is a",
            [
                "Asset",
                "Liability",
                "Expense",
                "Loss"
            ]
        )

        if st.button("Submit"):

            if answer == "Liability":

                st.success("Correct")

            else:

                st.error("Wrong")

    # BOARD PAPERS

    with student_tabs[3]:

        st.subheader("📄 Board Papers")

        st.info("Board Papers Coming Soon")

    # STUDY ROOM

    with student_tabs[4]:

        st.subheader("🎥 Study Room")

        video_link = st.text_input(
            "Enter YouTube Link"
        )

        if video_link:

            st.video(video_link)

# ====================================================
# ADMIN
# ====================================================

with main_tabs[1]:

    st.header("👨‍🏫 Admin Dashboard")

    admin_tabs = st.tabs([
        "📝 Paper Generator",
        "📤 Upload Questions",
        "📊 Results"
    ])

    # PAPER GENERATOR

    with admin_tabs[0]:

        st.subheader("📝 Paper Generator")

        subject = st.selectbox(
            "Select Subject",
            [
                "Book Keeping",
                "OCM",
                "SP"
            ]
        )

        marks = st.number_input(
            "Total Marks",
            value=80
        )

        if st.button("Generate Paper"):

            st.success("Paper Generated")

            st.write(f"""
            Subject: {subject}

            Total Marks: {marks}

            Q1. Objective Questions

            Q2. Short Notes

            Q3. Practical Problem
            """)

    # UPLOAD QUESTIONS

    with admin_tabs[1]:

        st.subheader("📤 Upload Questions")

        uploaded_csv = st.file_uploader(
            "Upload CSV",
            type=["csv"]
        )

        if uploaded_csv:

            df = pd.read_csv(uploaded_csv)

            st.dataframe(df)

    # RESULTS

    with admin_tabs[2]:

        st.subheader("📊 Results")

        st.metric("Students", 120)

        st.metric("Average Score", "72%")
