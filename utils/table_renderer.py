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
    ">
    """

    for r_idx, row in enumerate(table_data):

        html += "<tr>"

        for col in row:

            if r_idx == 0:

                html += f"""
                <th style="
                    border:1px solid #ccc;
                    padding:10px;
                    background:#374151;
                    color:white;
                    text-align:center;
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
