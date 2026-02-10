import pandas as pd
import streamlit as st
from snowflake.connector import connect

st.title("Snowflake Streamlit Test")

st.write("Connecting to Snowflake...")

conn = connect(**st.secrets["snowflake"])

st.success("Connected successfully")

query = "SELECT * FROM ENTERPRISE_DB.GOLD.CUSTOMERS LIMIT 100"
st.write("Running query:", query)

df = pd.read_sql(query, conn)

st.dataframe(df)
