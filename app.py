import streamlit as st
import pandas as pd

# ====================================================
# PAGE CONFIG
# ====================================================
st.set_page_config(page_title="Mitradnya Learning Platform", layout="wide")

# ====================================================
# HELPER FUNCTIONS
# ====================================================
def render_html_table(data):
    """टेबल रेंडर करण्यासाठी फंक्शन"""
    if not data:
        return
    
    html = "<table style='width:100%; border-collapse:collapse; margin-bottom:15px;'>"
    for r_idx, t_row in enumerate(data):
        html += "<tr>"
        for col in t_row:
            if r_idx == 0:
                html += f"<th style='border:1px solid #ddd; padding:10px; background:#374151; color:white; text-align:center;'>{col}</th>"
            else:
                html += f"<td style='border:1px solid #ddd; padding:10px;'>{col}</td>"
        html += "</tr>"
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)

# ====================================================
# TITLE
# ====================================================
st.title("📚 Mitradnya Learning Platform 📚")

# ====================================================
# MAIN TABS
# ====================================================
main_tabs = st.tabs(["🎓 Student Dashboard", "👨‍🏫 Admin Dashboard"])

# ====================================================
# STUDENT DASHBOARD
# ====================================================
with main_tabs[0]:
    st.header("🎓 Student Dashboard")
    student_tabs = st.tabs(["📖 Notes", "📝 Questions", "🎯 MCQ", "🎥 Study Room"])

    # 1. NOTES
    with student_tabs[0]:
        st.subheader("📖 Notes")
        uploaded_notes = st.file_uploader("Upload PDF Notes", type=["pdf"])
        if uploaded_notes:
            st.success("Notes Uploaded Successfully")

    # 2. QUESTIONS
    with student_tabs[1]:
        st.subheader("📝 Questions")
        try:
            df = pd.read_csv("data/QnA.csv")
            df.columns = df.columns.str.strip()
            
            df["Chapter_Name"] = df["Chapter_Name"].ffill()
            df["Category"] = df["Category"].ffill()
            
            df["is_main"] = df["Question_Text"].astype(str).str.contains("Q1|Q2|Q3|Q4|Q5", na=False)
            df["Question_ID"] = df["is_main"].cumsum()

            chapter = st.selectbox("Select Chapter", df["Chapter_Name"].unique())
            category = st.selectbox("Select Category", df["Category"].unique())

            filtered_df = df[(df["Chapter_Name"] == chapter) & (df["Category"] == category)]
            grouped = filtered_df.groupby("Question_ID")

            for q_id, group in grouped:
                with st.container():
                    st.markdown(f"""
                    <div style="padding:15px; border:1px solid #ddd; border-radius:10px; margin-bottom:20px; background-color:#111827;">
                    <h4 style="color:white;">Question {q_id}</h4>
                    </div>
                    """, unsafe_allow_html=True)

                    with st.expander(f"📘 Open Question {q_id}"):
                        table_data = []
                        for _, row in group.iterrows():
                            line = str(row["Question_Text"]).strip()
                            if "|" in line:
                                table_data.append([c.strip() for c in line.split("|")])
                            else:
                                if table_data:
                                    render_html_table(table_data)
                                    table_data = []
                                if line:
                                    st.markdown(f"""
                                    <div style="padding:8px; margin-bottom:8px; border-radius:6px; background:#1f2937;">
                                    {line}
                                    </div>
                                    """, unsafe_allow_html=True)
                        if table_data:
                            render_html_table(table_data)

        except Exception as e:
            st.error(f"माहिती लोड करताना त्रुटी आली: {e}")

    # 3. MCQ & 4. STUDY ROOM
    with student_tabs[2]:
        st.subheader("🎯 MCQ Test")
        st.info("MCQ Section Working")
    with student_tabs[3]:
        st.subheader("🎥 Study Room")
        st.info("Study Room Working")

# ====================================================
# ADMIN DASHBOARD
# ====================================================

with main_tabs[1]:

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

        st.subheader("📤 Upload CSV File")

        uploaded_file = st.file_uploader(
            "Upload QnA CSV",
            type=["csv"]
        )

        if uploaded_file:

            try:

                df_upload = pd.read_csv(uploaded_file)

                st.success("CSV Uploaded Successfully")

                st.dataframe(df_upload.head())

            except Exception as e:

                st.error(e)

    # ====================================================
    # VIEW DATABASE
    # ====================================================

    with admin_tabs[1]:

        st.subheader("📊 Question Database")

        try:

            df_db = pd.read_csv("data/QnA.csv")

            df_db.columns = df_db.columns.str.strip()

            st.write("Total Questions:", len(df_db))

            st.dataframe(
                df_db,
                use_container_width=True
            )

        except Exception as e:

            st.error(e)

    # ====================================================
    # ADD QUESTION
    # ====================================================

    with admin_tabs[2]:

        st.subheader("📝 Add New Question")

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

        if st.button("➕ Save Question"):

            try:

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

                st.success(
                    "Question Saved Successfully"
                )

            except Exception as e:

                st.error(e)

    # ====================================================
    # CREATE QUESTION GROUPS
    # ====================================================
    df["Question_Text"] = (df["Question_Text.astype(str))

    # MAIN QUESTION DETECTION
                           df["is_main"] = df["Question_Text"].str.contains(r"Q\d",regex=True,na=False)

# QUESTION ID
df["Question_ID"] = (
    df["is_main"]
    .cumsum()
)

# FILL VALUES
df["Chapter_Name"] = (
    df["Chapter_Name"]
    .ffill()
)

df["Category"] = (
    df["Category"]
    .ffill()
)
    # ====================================================
    # STATISTICS
    # ====================================================

    with admin_tabs[3]:

        st.subheader("📈 Statistics")

        try:

            stats_df = pd.read_csv(
                "data/QnA.csv"
            )

            total_questions = len(stats_df)

            total_chapters = stats_df[
                "Chapter_Name"
            ].nunique()

            total_categories = stats_df[
                "Category"
            ].nunique()

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Questions",
                    total_questions
                )

            with col2:

                st.metric(
                    "Chapters",
                    total_chapters
                )

            with col3:

                st.metric(
                    "Categories",
                    total_categories
                )

        except Exception as e:

            st.error(e)
