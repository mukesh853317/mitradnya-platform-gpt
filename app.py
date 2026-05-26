import streamlit as st
import pandas as pd

# PAGE
st.set_page_config(
    page_title="Mitradnya",
    layout="wide"
)

st.title("📚 Mitradnya Learning Platform")

# LOAD CSV
df = pd.read_csv("data/QnA.csv")

# CLEAN COLUMNS
df.columns = df.columns.str.strip()

# FILL EMPTY
df["Chapter_Name"] = df["Chapter_Name"].ffill()
df["Category"] = df["Category"].ffill()

# FILTERS
chapter = st.selectbox(
    "Select Chapter",
    df["Chapter_Name"].unique()
)

category = st.selectbox(
    "Select Category",
    df["Category"].unique()
)

# FILTER DATA
filtered_df = df[
    (df["Chapter_Name"] == chapter)
    &
    (df["Category"] == category)
]

# SHOW QUESTIONS
for idx, row in filtered_df.iterrows():

    question = str(row["Question_Text"])

    # TABLE FORMAT
    if "|" in question:

        cols = question.split("|")

        html = "<table style='width:100%; border-collapse:collapse;'>"
        html += "<tr>"

        for c in cols:

            html += f"""
            <td style='
            border:1px solid #ccc;
            padding:10px;
            '>
            {c}
            </td>
            """

        html += "</tr></table>"

        st.markdown(
            html,
            unsafe_allow_html=True
        )

    else:

        st.markdown(f"""
        <div style="
        padding:10px;
        margin-bottom:10px;
        border-radius:10px;
        background:#1f2937;
        color:white;
        ">
        {question}
        </div>
        """, unsafe_allow_html=True)
