import streamlit as st
import pandas as pd


def show_admin_dashboard():

    st.header("👨‍🏫 Admin Dashboard")

    tabs = st.tabs([
        "📊 Database",
        "➕ Add Question"
    ])

    # ============================================
    # DATABASE
    # ============================================

    with tabs[0]:

        st.subheader("📊 Question Database")

        try:

            df = pd.read_csv("data/QnA.csv")

            st.dataframe(
                df,
                use_container_width=True
            )

        except Exception as e:

            st.error(e)

    # ============================================
    # ADD QUESTION
    # ============================================

    with tabs[1]:

        st.subheader("➕ Add Question")

        chapter = st.text_input(
            "Chapter"
        )

        category = st.selectbox(
            "Category",
            [
                "IMP_Proforma",
                "Short_Notes",
                "One_Sentence",
                "Exercise_Problems",
                "Extra_Practical"
            ]
        )

        question = st.text_area(
            "Question"
        )

        answer = st.text_area(
            "Answer"
        )

        if st.button("Save"):

            new_row = pd.DataFrame({

                "Chapter_Name": [chapter],
                "Category": [category],
                "Question_Text": [question],
                "Answer_or_Hint": [answer]

            })

            try:

                old_df = pd.read_csv(
                    "data/QnA.csv"
                )

                updated_df = pd.concat(
                    [old_df, new_row],
                    ignore_index=True
                )

            except:

                updated_df = new_row

            updated_df.to_csv(
                "data/QnA.csv",
                index=False
            )

            st.success(
                "Question Saved Successfully"
            )
