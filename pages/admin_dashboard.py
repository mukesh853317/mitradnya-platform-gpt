import streamlit as st
import pandas as pd

def show_admin_dashboard():

    st.header("👨‍🏫 Admin Dashboard")

    admin_tabs = st.tabs([
        "📤 Upload Questions",
        "📊 View Database",
        "📝 Add Question",
        "📈 Statistics"
    ])

    # ====================================================
    # UPLOAD CSV
    # ====================================================

    with admin_tabs[0]:

        st.subheader("📤 Upload CSV")

        uploaded_file = st.file_uploader(
            "Upload CSV",
            type=["csv"]
        )

        if uploaded_file:

            df = pd.read_csv(uploaded_file)

            st.success("Uploaded Successfully")

            st.dataframe(df)

    # ====================================================
    # VIEW DATABASE
    # ====================================================

    with admin_tabs[1]:

        st.subheader("📊 Database")

        try:

            df = pd.read_csv("data/QnA.csv")

            st.dataframe(
                df,
                use_container_width=True
            )

        except Exception as e:

            st.error(e)

    # ====================================================
    # ADD QUESTION
    # ====================================================

    with admin_tabs[2]:

        st.subheader("📝 Add Question")

        chapter = st.text_input(
            "Chapter Name"
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
            "Answer / Hint"
        )

        if st.button("Save Question"):

            new_data = pd.DataFrame({

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
                    [old_df, new_data],
                    ignore_index=True
                )

            except:

                updated_df = new_data

            updated_df.to_csv(
                "data/QnA.csv",
                index=False
            )

            st.success("Saved Successfully")

    # ====================================================
    # STATS
    # ====================================================

    with admin_tabs[3]:

        st.subheader("📈 Statistics")

        try:

            df = pd.read_csv("data/QnA.csv")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Questions",
                len(df)
            )

            col2.metric(
                "Chapters",
                df["Chapter_Name"].nunique()
            )

            col3.metric(
                "Categories",
                df["Category"].nunique()
            )

        except Exception as e:

            st.error(e)
