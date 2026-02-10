import pandas as pd
import streamlit as st
from snowflake.connector import connect

st.title("Snowflake Streamlit Test")

conn = connect(**st.secrets["snowflake"])

query = "SELECT * FROM ENTERPRISE_DB.GOLD.YOUR_TABLE LIMIT 100"
df = pd.read_sql(query, conn)

st.dataframe(df)
