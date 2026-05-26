import streamlit as st

def render_html_table(data):

    if not data:
        return

    html = """
    <table style="
        width:100%;
        border-collapse:collapse;
        margin-bottom:20px;
        background:white;
        color:black;
        font-size:15px;
    ">
    """

    for r_idx, row in enumerate(data):

        html += "<tr>"

        for col in row:

            if r_idx == 0:

                html += f"""
                <th style="
                    border:1px solid #ccc;
                    padding:10px;
                    background:#1f2937;
                    color:white;
                    text-align:center;
                    font-weight:bold;
                ">
                    {col}
                </th>
                """

            else:

                html += f"""
                <td style="
                    border:1px solid #ccc;
                    padding:10px;
                    text-align:left;
                ">
                    {col}
                </td>
                """

        html += "</tr>"

    html += "</table>"

    st.markdown(html, unsafe_allow_html=True)
