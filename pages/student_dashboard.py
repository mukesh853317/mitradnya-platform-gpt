import streamlit as st
import pandas as pd

from utils.table_renderer import render_html_table


def show_student_dashboard():

    st.header("🎓 Student Dashboard")

    student_tabs = st.tabs([
        "📝 Questions",
        "🎯 MCQ",
        "🎥 Study Room"
    ])

    # ==================================================
    # QUESTIONS
    # ==================================================

    with student_tabs[0]:

        st.subheader("📝 Questions")

        try:

            df = pd.read_csv("data/QnA.csv")

            df.columns = df.columns.str.strip()

            df["Chapter_Name"] = df["Chapter_Name"].ffill()
            df["Category"] = df["Category"].ffill()

            # Main Question Detection
            df["is_main"] = (
                df["Question_Text"]
                .astype(str)
                .str.contains(
                    r"From the following|Q1|Q2|Q3|Q4",
                    regex=True,
                    na=False
                )
            )

            df["Question_ID"] = (
                df["is_main"]
                .cumsum()
            )

            chapter = st.selectbox(
                "Select Chapter",
                df["Chapter_Name"].dropna().unique()
            )

            category = st.selectbox(
                "Select Category",
                df["Category"].dropna().unique()
            )

            filtered_df = df[
                (df["Chapter_Name"] == chapter)
                &
                (df["Category"] == category)
            ]

            grouped = filtered_df.groupby("Question_ID")

            for q_no, (qid, group) in enumerate(grouped, start=1):

                first_question = str(
                    group.iloc[0]["Question_Text"]
                )

                title = (
                    first_question[:80] + "..."
                    if len(first_question) > 80
                    else first_question
                )

                with st.expander(f"📘 Question {q_no}: {title}"):

                    table_data = []

                    for _, row in group.iterrows():

                        line = str(
                            row["Question_Text"]
                        ).strip()

                        # TABLE LINE
                        if "|" in line:

                            cols = [
                                c.strip()
                                for c in line.split("|")
                            ]

                            table_data.append(cols)

                        else:

                            # Render Previous Table
                            if table_data:

                                render_html_table(
                                    table_data
                                )

                                table_data = []

                            if line:

                                st.markdown(line)

                    # Final Table Render
                    if table_data:

                        render_html_table(
                            table_data
                        )

        except Exception as e:

            st.error(f"Error: {e}")

    # ==================================================
    # MCQ
    # ==================================================

    with student_tabs[1]:

        st.subheader("🎯 MCQ Test")

        st.info("MCQ Section Ready")

    # ==================================================
    # STUDY ROOM
    # ==================================================

    with student_tabs[2]:

        st.subheader("🎥 Study Room")

        st.markdown("""
        ### 📚 Smart Study Room

        - Watch Lectures
        - Revise Daily
        - Track Progress
        - Focus Mode
        """)

        subject = st.selectbox(
            "Select Subject",
            [
                "Book Keeping",
                "OCM",
                "SP",
                "Economics"
            ]
        )

        chapter_name = st.text_input(
            "Enter Chapter Name"
        )

        study_time = st.slider(
            "Study Time (Minutes)",
            15,
            180,
            45
        )

        st.info(
            f"🎯 Today's Focus Session: {study_time} Minutes"
        )

        notes = st.text_area(
            "Quick Notes"
        )

        if st.button("💾 Save Notes"):

            st.success("Notes Saved")
