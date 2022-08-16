import streamlit as st


class SqlInput:
    def __init__(self) -> None:
        self._subheader()
        self._input_area()

    def _subheader(self):
        st.subheader(f"Enter your SQL query here:")

    def _input_area(self):
        query = """
            SELECT product_id,
                Count(star_rating) as total_rating,
                Max(star_rating)   AS best_rating,
                Min(star_rating)   AS worst_rating
            FROM   tbl_books
            WHERE  verified_purchase = 'Y'
                AND review_date BETWEEN '1995-07-22' AND '2015-08-31'
                AND marketplace IN ( 'DE', 'US', 'UK', 'FR', 'JP' )
            GROUP  BY product_id
            ORDER  BY total_rating asc,product_id desc,best_rating
            LIMIT  10;
        """
        sql_input = st.text_input(label="your sql query", key="sql_input", value=query)
        st.code(sql_input, language="sql")
