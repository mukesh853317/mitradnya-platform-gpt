import streamlit as st
                df,
                use_container_width=True
            )

        except Exception as e:

            st.error(e)

    # ====================================================
    # ADD QUESTION
    # ====================================================

    with tabs[2]:

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
            "Answer"
        )

        if st.button("Save Question"):

            new_df = pd.DataFrame({
                "Chapter_Name": [chapter],
                "Category": [category],
                "Question_Text": [question],
                "Answer_or_Hint": [answer]
            })

            try:

                old_df = pd.read_csv(
                    "data/QnA.csv"
                )

                final_df = pd.concat(
                    [old_df, new_df],
                    ignore_index=True
                )

            except:

                final_df = new_df
