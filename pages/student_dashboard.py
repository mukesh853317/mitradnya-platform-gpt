import streamlit as st
                        key=f"solution_{q_id}"
                    ):

                        with st.spinner(
                            "Generating Solution..."
                        ):

                            answer = generate_solution(
                                full_question
                            )

                            st.success(
                                "Solution Generated"
                            )

                            st.write(answer)

        except Exception as e:

            st.error(e)

    # ====================================================
    # MCQ
    # ====================================================

    with tabs[2]:

        st.subheader("🎯 MCQ Test")

        st.info("MCQ Module Ready")

    # ====================================================
    # STUDY ROOM
    # ====================================================

    with tabs[3]:

        st.subheader("🎥 Study Room")

        subject = st.selectbox(
            "Select Subject",
            [
                "Book Keeping",
                "OCM",
                "SP",
                "Economics"
            ]
        )

        st.write(f"Selected Subject: {subject}")

        timer = st.slider(
            "Study Time",
            15,
            180,
            45
        )

        st.progress(0)

        st.info(
            f"Focus Session: {timer} Minutes"
        )
