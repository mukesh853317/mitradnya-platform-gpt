import google.generativeai as genai
import streamlit as st


def generate_solution(question):

    try:

        genai.configure(
            api_key=st.secrets["GOOGLE_API_KEY"]
        )

        model = genai.GenerativeModel(
            "gemini-1.5-flash"
        )

        prompt = f"""
        You are Maharashtra Board Commerce Teacher.

        Solve the following question:

        Rules:
        - step by step
        - easy language
        - proper board format
        - detailed explanation

        Question:
        {question}
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"AI Error: {e}"
