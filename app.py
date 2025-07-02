import streamlit as st 
import pandas as pd 
import duckdb as db

st.write("SQL Practice")

module = st.selectbox(
    "What would you like to review ?",
    ("Joins", "GroupBY", "Windows functions"),
    index = None,
    placeholder="Select a theme ..."
)

df = pd.DataFrame({
    "event" : ["session_start", "click", "download_file", "purchase"],
    "event_count" : [1140, 8512, 23, 12]
})

query = st.text_area(label="Enter your sql query")

st.dataframe(df)

if query :
    st.write(f"Vous avez entré la query : {query}")
    res = db.query(query)
    st.dataframe(res)



