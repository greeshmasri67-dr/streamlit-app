import streamlit as st
import snowflake.connector
import pandas as pd

st.set_page_config(page_title="Streamlit + Snowflake")

st.title("❄️ Streamlit connected to Snowflake")

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=st.secrets["snowflake"]["user"],
    password=st.secrets["snowflake"]["password"],
    account=st.secrets["snowflake"]["account"],
    warehouse=st.secrets["snowflake"]["warehouse"],
    database=st.secrets["snowflake"]["database"],
    schema=st.secrets["snowflake"]["schema"],
    role=st.secrets["snowflake"]["role"]
)

# Run query
query = "SELECT CURRENT_USER(), CURRENT_DATE();"
df = pd.read_sql(query, conn)

st.success("✅ Connected to Snowflake")
st.dataframe(df)
