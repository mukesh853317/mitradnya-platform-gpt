import streamlit as st
        )

        completed = st.slider(
            "Completed Questions",
            0,
            total,
            5
        )

        progress = completed / total

        st.progress(progress)

        st.write(
            f"✅ Progress: {completed}/{total}"
        )


# ====================================================
# ADMIN DASHBOARD
# ====================================================

with main_tabs[1]:

    st.header("👨‍🏫 Admin Dashboard")

    admin_tabs = st.tabs([
        "📝 Paper Generator",
        "📤 Upload Questions",
        "📊 Analytics"
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
                "Economics"
            ]
        )

        marks = st.number_input(
            "Total Marks",
            value=80
        )

        if st.button("Generate Paper"):

            st.success("Paper Generated")

            st.markdown(f"""
            ### 📄 {subject} Question Paper

            Total Marks: {marks}

            Q1. Objective Questions

            Q2. Short Notes

            Q3. Practical Problems
