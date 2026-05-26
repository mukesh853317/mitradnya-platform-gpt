import streamlit as st

def render_html_table(table_data):

    if not table_data:
        return

    html = """
    <table style="
        width:100%;
        border-collapse:collapse;
        margin-top:10px;
        margin-bottom:20px;
        font-size:15px;
    ">
    """

    for r_idx, row in enumerate(table_data):

        html += "<tr>"

        for col in row:

            if r_idx == 0:

                html += f"""
                <th style="
                    border:1px solid #d1d5db;
                    padding:10px;
                    background-color:#374151;
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
                    border:1px solid #d1d5db;
                    padding:10px;
                    background:white;
                    color:black;
                ">
                    {col}
                </td>
                """

        html += "</tr>"

    html += "</table>"

    st.markdown(
        html,
        unsafe_allow_html=True
    )
