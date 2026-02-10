import streamlit as st
import pandas as pd
import snowflake.connector

st.set_page_config(page_title="Streamlit + Snowflake", layout="wide")

st.title("❄️ Streamlit connected to Snowflake")

# 1️⃣ Connect to Snowflake
conn = snowflake.connector.connect(
    user=st.secrets["snowflake"]["user"],
    password=st.secrets["snowflake"]["password"],
    account=st.secrets["snowflake"]["account"],
    warehouse=st.secrets["snowflake"]["warehouse"],
    database=st.secrets["snowflake"]["database"],
    schema=st.secrets["snowflake"]["schema"],
    role=st.secrets["snowflake"]["role"]
)

st.success("✅ Connected successfully")

# 2️⃣ Run query using cursor (MOST RELIABLE)
query = """
SELECT *
FROM ENTERPRISE_DB.GOLD.CUSTOMER_DATA
LIMIT 100
"""

cur = conn.cursor()
cur.execute(query)

# Fetch data
data = cur.fetchall()
columns = [desc[0] for desc in cur.description]

df = pd.DataFrame(data, columns=columns)

# 3️⃣ Show data
st.subheader("📄 Data Preview")
st.dataframe(df)

# 4️⃣ Simple graph (example)
if len(df.columns) >= 2:
    st.subheader("📊 Sample Chart")
    st.bar_chart(df.iloc[:, 1])

cur.close()
conn.close()
