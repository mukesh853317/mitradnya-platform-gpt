import streamlit as st
import pandas as pd

# ====================================================
# PAGE CONFIG
# ====================================================
st.set_page_config(page_title="Mitradnya Learning Platform", layout="wide")

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

    # NOTES
    with student_tabs[0]:
        st.subheader("📖 Notes")
        uploaded_notes = st.file_uploader("Upload PDF Notes", type=["pdf"])
        if uploaded_notes:
            st.success("Notes Uploaded Successfully")

    # QUESTIONS
    with student_tabs[1]:
        st.subheader("📝 Questions")
        try:
            df = pd.read_csv("data/QnA.csv")
            df.columns = df.columns.str.strip()
            
            # Fill missing values
            df["Chapter_Name"] = df["Chapter_Name"].ffill()
            df["Category"] = df["Category"].ffill()
            
            # Main Question Detection
            df["is_main"] = df["Question_Text"].astype(str).str.contains("Q1|Q2|Q3|Q4|Q5", na=False)
            df["Question_ID"] = df["is_main"].cumsum()

            # Chapter Select
            chapter = st.selectbox("Select Chapter", df["Chapter_Name"].unique())
            
            # Category Select
            category = st.selectbox("Select Category", df["Category"].unique())

            filtered_df = df[(df["Chapter_Name"] == chapter) & (df["Category"] == category)]
            grouped = filtered_df.groupby("Question_ID")

            for q_id, group in grouped:
                first_row = group.iloc[0]
                title = first_row["Question_Text"]

import streamlit as st

# टेबल रेंडर करण्यासाठी एक फंक्शन (कोडची पुनरावृत्ती टाळण्यासाठी)
def render_html_table(data):
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

# Main logic inside your loop
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
                cols = [c.strip() for c in line.split("|")]
                table_data.append(cols)
            else:
                # जर टेबल डेटा असेल तर आधी तो प्रिंट करा
                if table_data:
                    render_html_table(table_data)
                    table_data = [] # डेटा रिकामा करा
                
                # नॉर्मल टेक्स्ट प्रिंट करा
                if line:
                    st.markdown(f"""
                    <div style="padding:8px; margin-bottom:8px; border-radius:6px; background:#1f2937;">
                    {line}
                    </div>
                    """, unsafe_allow_html=True)

        # शेवटी राहिलेला टेबल डेटा प्रिंट करा
        if table_data:
            render_html_table(table_data)

                    # Last Table handling
                    if table_data:
                        table_html = "<table style='width:100%; border-collapse:collapse; margin-bottom:15px;'>"
                        for r_idx, t_row in enumerate(table_data):
                            table_html += "<tr>"
                            for col in t_row:
                                if r_idx == 0:
                                    table_html += f"<th style='border:1px solid #ddd; padding:8px; background:#262730; color:white;'>{col}</th>"
                                else:
                                    table_html += f"<td style='border:1px solid #ddd; padding:8px;'>{col}</td>"
                            table_html += "</tr>"
                        table_html += "</table>"
                        st.markdown(table_html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

    # MCQ
    with student_tabs[2]:
        st.subheader("🎯 MCQ Test")
        st.info("MCQ Section Working")

    # STUDY ROOM
    with student_tabs[3]:
        st.subheader("🎥 Study Room")
        st.info("Study Room Working")

# ====================================================
# ADMIN DASHBOARD
# ====================================================
with main_tabs[1]:
    st.header("👨‍🏫 Admin Dashboard")
    st.info("Admin Dashboard Working")
