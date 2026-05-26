import streamlit as st
import pandas as pd

# ====================================================
# PAGE CONFIG
# ====================================================

st.set_page_config(
    page_title="Mitradnya Learning Platform",
    layout="wide"
)

st.title("📚 Mitradnya Learning Platform")

# ====================================================
# LOAD CSV
# ====================================================

df = pd.read_csv("data/QnA.csv")

df.columns = df.columns.str.strip()

df["Chapter_Name"] = df["Chapter_Name"].ffill()
df["Category"] = df["Category"].ffill()

# ====================================================
# QUESTION ID
# ====================================================

df["is_main"] = (
    df["Question_Text"]
    .astype(str)
    .str.contains("Q1|Q2|Q3|Q4|Q5", na=False)
)

df["Question_ID"] = df["is_main"].cumsum()

# ====================================================
# TABLE FUNCTION
# ====================================================

def render_html_table(table_data):

    table_html = """
    <table style='
    width:100%;
    border-collapse:collapse;
    margin-bottom:15px;
    '>
    """

    for r_idx, t_row in enumerate(table_data):

        table_html += "<tr>"

        for col in t_row:

            if r_idx == 0:

                table_html += f"""
                <th style='
                border:1px solid #ddd;
                padding:10px;
                background:#374151;
                color:white;
                text-align:center;
                '>
                {col}
                </th>
                """

            else:

                table_html += f"""
                <td style='
                border:1px solid #ddd;
                padding:10px;
                '>
                {col}
                </td>
                """

        table_html += "</tr>"

    table_html += "</table>"

    st.markdown(
        table_html,
        unsafe_allow_html=True
    )

# ====================================================
# FILTERS
# ====================================================

chapter = st.selectbox(
    "📘 Select Chapter",
    df["Chapter_Name"].unique()
)

category = st.selectbox(
    "📚 Select Category",
    df["Category"].unique()
)

filtered_df = df[
    (df["Chapter_Name"] == chapter)
    &
    (df["Category"] == category)
]

grouped = filtered_df.groupby("Question_ID")

# ====================================================
# QUESTIONS
# ====================================================

for q_id, group in grouped:

    first_row = group.iloc[0]

    title = str(first_row["Question_Text"])

    with st.container():

        st.markdown(f"""
        <div style="
        padding:15px;
        border:1px solid #ddd;
        border-radius:10px;
        margin-bottom:20px;
        background:#111827;
        ">
        <h3 style="color:white;">
        Question {q_id}
        </h3>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📖 Open Question"):

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

                    # SHOW TABLE
                    if table_data:

                        render_html_table(table_data)

                        table_data = []

                    # NORMAL TEXT
                    if line:

                        st.markdown(f"""
                        <div style="
                        padding:8px;
                        margin-bottom:8px;
                        border-radius:6px;
                        background:#1f2937;
                        color:white;
                        ">
                        {line}
                        </div>
                        """, unsafe_allow_html=True)

            # LAST TABLE
            if table_data:

                render_html_table(table_data)
