import streamlit as st

from pages.student_dashboard import show_student_dashboard
from pages.admin_dashboard import show_admin_dashboard

st.set_page_config(
    page_title="Mitradnya Learning Platform",
    layout="wide"
)

st.title("📚 Mitradnya Learning Platform")

main_tabs = st.tabs([
    "🎓 Student Dashboard",
    "👨‍🏫 Admin Dashboard"
])

with main_tabs[0]:
    show_student_dashboard()

with main_tabs[1]:
    show_admin_dashboard()
