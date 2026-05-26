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

    # ====================================================
    # QUESTIONS
    # ====================================================

    with student_tabs[0]:

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
                .str.contains(r"Q\d", regex=True, na=False)
            )

            # QUESTION GROUPS

            df["Question_ID"] = (
                df["is_main"]
                .cumsum()
            )

            # FILTERS

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

            # QUESTIONS

            for q_no, group in grouped:

                first_row = group.iloc[0]

                title = str(
                    first_row["Question_Text"]
                )

                short_title = (
                    title[:80] + "..."
                    if len(title) > 80
                    else title
                )

                with st.expander(f"📘 {short_title}"):

                    table_data = []

                    for _, row in group.iterrows():

                        line = str(
                            row["Question_Text"]
                        ).strip()

                        # TABLE LINE

                        if "|" in line:

                            row_data = [
                                col.strip()
                                for col in line.split("|")
                            ]

                            table_data.append(row_data)

                        else:

                            if table_data:

                                render_html_table(
                                    table_data
                                )

                                table_data = []

                            if line:

                                st.markdown(line)

                    # LAST TABLE

                    if table_data:

                        render_html_table(
                            table_data
                        )

        except Exception as e:

            st.error(e)

    # ====================================================
    # MCQ
    # ====================================================

    with student_tabs[1]:

        st.subheader("🎯 MCQ Test")

        st.info("MCQ Section Working")

    # ====================================================
    # STUDY ROOM
    # ====================================================

    with student_tabs[2]:

        st.subheader("🎥 Study Room")

        st.info("Study Room Working")
