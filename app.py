import streamlit as st
import pandas as pd
import google.generativeai as genai

# ====================================================
# GEMINI API
# ====================================================

API_KEY = " "

genai.configure(api_key=API_KEY)

# ====================================================
# PAGE CONFIG
# ====================================================

st.set_page_config(
    page_title="Mitradnya Learning Platform",
    layout="wide"
)

st.title("📚 Mitradnya Learning Platform")

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
        "📄 Board Papers",
        "🎥 Study Room"
    ])

    # ====================================================
    # NOTES
    # ====================================================

    with student_tabs[0]:

        st.subheader("📖 Notes")

        uploaded_notes = st.file_uploader(
            "Upload Notes",
            type=["pdf"]
        )

        if uploaded_notes:

            st.success("Notes Uploaded Successfully")

    # ====================================================
    # QUESTIONS
    # ====================================================

with student_tabs[1]:

    st.subheader("📝 Questions")

    df = pd.read_csv("data/qna.csv")

    df.columns = df.columns.str.strip()

    chapter = st.selectbox(
        "Select Chapter",
        df["Chapter_Name"].dropna().unique()
    )

    filtered_df = df[
        df["Chapter_Name"] == chapter
    ]

    question = st.selectbox(
        "Select Question",
        filtered_df["Question_Text"].dropna()
    )

    st.code(question)

    if st.button("Show AI Solution"):

        with st.spinner("Generating Solution..."):

            try:

                model = genai.GenerativeModel(
                    "gemini-2.0-flash"
                )

                prompt = f"""
                Solve this Maharashtra Board question.

                Use:
                - proper format
                - step-by-step explanation
                - easy language
                - board pattern

                Question:
                {question}
                """

                response = model.generate_content(
                    prompt
                )

                st.success("Solution Generated")

                st.write(response.text)

            except Exception as e:

                st.error(e)

    # ====================================================
    # MCQ TEST
    # ====================================================

    with student_tabs[2]:

        st.subheader("🎯 MCQ Test")

        mcq_df = pd.read_csv(
    "data/mcq.csv",
    encoding="utf-8"
)

random_question = mcq_df.sample(1).iloc[0]

st.write(random_question["Question"])

answer = st.radio(
    "Choose Answer",
    [
        random_question["Option A"],
        random_question["Option B"],
        random_question["Option C"],
        random_question["Option D"]
    ]
)

if st.button("Submit MCQ"):

    correct = random_question[
        "Correct Answer (Full Text)"
    ]

    if answer == correct:

        st.success("Correct Answer")

    else:

        st.error(f"Correct Answer: {correct}")
        
        if uploaded_mcq:

            mcq_df = pd.read_csv(
                uploaded_mcq,
                encoding="utf-8"
            )

            random_question = mcq_df.sample(1).iloc[0]

            st.write(random_question["Question"])

            answer = st.radio(
                "Choose Answer",
                [
                    random_question["Option A"],
                    random_question["Option B"],
                    random_question["Option C"],
                    random_question["Option D"]
                ]
            )

            if st.button("Submit MCQ"):

                correct = random_question[
                    "Correct Answer (Full Text)"
                ]

                if answer == correct:

                    st.success("Correct Answer")

                else:

                    st.error(
                        f"Correct Answer: {correct}"
                    )

    # ====================================================
    # BOARD PAPERS
    # ====================================================

    with student_tabs[3]:

        st.subheader("📄 Board Papers")

        st.info("Board Papers Will Be Added Here")

    # ====================================================
    # STUDY ROOM
    # ====================================================

    with student_tabs[4]:

        st.subheader("🎥 Study Room")

        video_link = st.text_input(
            "Enter YouTube Video Link"
        )

        if video_link:

            st.video(video_link)

# ====================================================
# ADMIN DASHBOARD
# ====================================================

with main_tabs[1]:

    st.header("👨‍🏫 Admin Dashboard")

    admin_tabs = st.tabs([
        "📝 Paper Generator",
        "📤 Upload Questions",
        "📊 Results"
    ])

    # ====================================================
    # PAPER GENERATOR
    # ====================================================

    with admin_tabs[0]:

        st.subheader("📝 Paper Generator")

        subject = st.selectbox(
            "Select Subject",
            [
                "Book Keeping",
                "OCM",
                "SP",
                "ECO"
            ]
        )

        marks = st.number_input(
            "Total Marks",
            value=80
        )

        if st.button("Generate Paper"):

            st.success("Paper Generated Successfully")

            st.write(f"""
            Subject: {subject}

            Total Marks: {marks}

            Q1. Objective Questions

            Q2. Short Notes

            Q3. Practical Problems

            Q4. Long Answers
            """)

    # ====================================================
    # UPLOAD QUESTIONS
    # ====================================================

    with admin_tabs[1]:

        st.subheader("📤 Upload Questions")

        uploaded_csv = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )

        if uploaded_csv:

            df = pd.read_csv(uploaded_csv)

            st.success("Questions Uploaded")

            st.dataframe(df)

    # ====================================================
    # RESULTS
    # ====================================================

    with admin_tabs[2]:

        st.subheader("📊 Student Results")

        st.metric("Students", 120)

        st.metric("Average Score", "72%")
