import streamlit as st
from loguru import logger

from converter.converter import converter_main
from .pyspark_output import PysparkOutput


class GenerateButton:
    def __init__(self) -> None:
        self._button()

    def _button(self):

        if st.button(
            label="GENERATE",
            key="GenerateButton",
        ):
            python_code = converter_main(st.session_state["sql_input"])
            PysparkOutput(python_code)
