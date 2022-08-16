import streamlit as st


class PysparkOutput:
    def __init__(self, python_code: str) -> None:
        container = st.container()
        container.subheader(f"PySpark Output")
        container.code(python_code, language="python")
