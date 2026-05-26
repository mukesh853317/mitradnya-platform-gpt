import streamlit as st

                            html_table += f"""
                            <td style='border:1px solid #ddd;
                            padding:8px;'>
                            {col}
                            </td>
                            """

                    html_table += "</tr>"

                html_table += "</table>"

                st.markdown(
                    html_table,
                    unsafe_allow_html=True
                )

                table_data = []

            if line:
                st.markdown(line)

    if table_data:

        html_table = """
        <table style='width:100%;
        border-collapse: collapse;
        margin-bottom:20px;'>
        """

        for r_idx, t_row in enumerate(table_data):

            html_table += "<tr>"

            for col in t_row:

                if r_idx == 0:

                    html_table += f"""
                    <th style='border:1px solid #ddd;
                    padding:8px;
                    background-color:#262730;
                    color:white;
                    text-align:center;'>
                    {col}
                    </th>
                    """

                else:

                    html_table += f"""
                    <td style='border:1px solid #ddd;
                    padding:8px;'>
                    {col}
                    </td>
                    """

            html_table += "</tr>"

        html_table += "</table>"

        st.markdown(
            html_table,
            unsafe_allow_html=True
        )
