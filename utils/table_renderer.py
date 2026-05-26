import streamlit as st


def render_html_table(data):

    if not data:
        return

    html = """
    <table style='width:100%;
    border-collapse:collapse;
    margin-bottom:20px;'>
    """

    for r_idx, row in enumerate(data):

        html += "<tr>"

        for col in row:

            if r_idx == 0:

                html += f"""
                <th style='border:1px solid #ddd;
                padding:10px;
                background:#374151;
                color:white;
                text-align:center;'>
                {col}
                </th>
                """

            else:

                html += f"""
                <td style='border:1px solid #ddd;
                padding:10px;'>
                {col}
                </td>
                """

        html += "</tr>"

    html += "</table>"

    st.markdown(html, unsafe_allow_html=True)
