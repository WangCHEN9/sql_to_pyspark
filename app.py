import streamlit as st
from components import PysparkOutput, GenerateButton, SqlInput


class App:
    def __init__(self) -> None:
        self._init_default_state()
        self._header()
        self._main()

    def _init_default_state(self):
        st.session_state[
            "output_code"
        ] = "'Click on generate button to get PySpark code'"

    def _header(self):
        st.header(f"sql to pyspark converter")

    def _main(self):

        SqlInput()

        GenerateButton()

        placeholder = st.empty()

        # PysparkOutput


if __name__ == "__main__":
    st.set_page_config(
        page_title="Sql to PySpark Converter",
        page_icon="🧊",
        layout="wide",
        menu_items={
            "Get Help": "https://www.wangchen.dev/",
            "Report a bug": "https://github.com/WangCHEN9/sql_to_pyspark/issues",
            "About": "# A Sql to PySpark Converter !",
        },
    )
    App()
