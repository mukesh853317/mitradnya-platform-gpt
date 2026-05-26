import streamlit as st
import pandas as pd

from utils.table_renderer import render_html_table


def show_student_dashboard():

    st.header("🎓 Student Dashboard")

    tabs = st.tabs([
        "📝 Questions",
        "🎯 MCQ",
        "🎥 Study Room"
    ])

    # =================================================
    # QUESTIONS
    # =================================================

    with tabs[0]:

        st.subheader("📝 Questions")

        try:

            df = pd.read_csv("data/QnA.csv")

            df.columns = df.columns.str.strip()

            df["Chapter_Name"] = df["Chapter_Name"].ffill()
            df["Category"] = df["Category"].ffill()

            # MAIN QUESTION DETECTION

            df["is_main"] = (
                df["Question_Text"]
                .astype(str)
                .str.contains(r"Q\d|From the following", regex=True, na=False)
            )

            df["Question_ID"] = df["is_main"].cumsum()

            chapter = st.selectbox(
                "Select Chapter",
                df["Chapter_Name"].unique()
            )

            category = st.selectbox(
                "Select Category",
                df["Category"].unique()
            )

            filtered_df = df[
                (df["Chapter_Name"] == chapter)
                &
                (df["Category"] == category)
            ]

            grouped = filtered_df.groupby("Question_ID")

            for q_no, group in grouped:

                first_question = str(
                    group.iloc[0]["Question_Text"]
                )

                short_title = (
                    first_question[:80] + "..."
                    if len(first_question) > 80
                    else first_question
                )

                with st.expander(f"📘 Question {q_no}: {short_title}"):

                    table_data = []

                    for _, row in group.iterrows():

                        line = str(row["Question_Text"]).strip()

                        # TABLE ROW

                        if "|" in line:

                            cols = [
                                c.strip()
                                for c in line.split("|")
                            ]

                            table_data.append(cols)

                        else:

                            # TABLE COMPLETE

                            if table_data:

                                render_html_table(
                                    table_data
                                )

                                table_data = []

                            # NORMAL TEXT

                            if line:

                                st.markdown(f"### {line})

                    # LAST TABLE

                    if table_data:

                        render_html_table(
                            table_data
                        )

        except Exception as e:

            st.error(e)

    # =================================================
    # MCQ
    # =================================================

    with tabs[1]:

        st.subheader("🎯 MCQ Test")

        st.info("MCQ Section")

    # =================================================
    # STUDY ROOM
    # =================================================

    with tabs[2]:

        st.subheader("🎥 Study Room")

        st.info("Study Room")
