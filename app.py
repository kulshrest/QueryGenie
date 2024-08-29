import os
import sqlite3
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("google_api_key"))

# Function to get Gemini response
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([prompt[0], question])
        sql_query = response.text.strip()
        # Clean up the SQL query
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
        sql_query = sql_query.replace('"', "'")
        if sql_query.lower().startswith("sql:"):
            sql_query = sql_query[4:].strip()
        return sql_query
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Function to execute SQL query and fetch results
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except Exception as e:
        return f"Error executing query: {str(e)}"

# Prompt for Generative AI
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.
    For example:
    - How many entries of records are present? 
      SQL: SELECT COUNT(*) FROM STUDENT;
    - Tell me all the students studying in Data Science class? 
      SQL: SELECT * FROM STUDENT WHERE CLASS='Data Science'; 
    Please ensure the SQL code does not include any formatting or unnecessary text.
    """
]

# Streamlit App Configuration
st.set_page_config(page_title="Gemini SQL Query App", page_icon="🔍")
st.title("Gemini SQL Query App")
st.subheader("Ask a question in natural language, and get the SQL query and results!")

# Input from the user
question = st.text_input("Enter your question:", key="input")

# Button to submit the question
if st.button("Generate SQL and Fetch Data"):
    if question:
        with st.spinner("Generating SQL query..."):
            sql_query = get_gemini_response(question, prompt)
            if "Error" in sql_query:
                st.error(sql_query)
            else:
                st.write("Generated SQL Query:")
                st.code(sql_query, language="sql")
                with st.spinner("Fetching data..."):
                    response = read_sql_query(sql_query, "student.db")
                    if isinstance(response, str) and "Error" in response:
                        st.error(response)
                    elif response:
                        st.subheader("Query Results:")
                        st.dataframe(response)
                    else:
                        st.warning("No data found for the given query.")
    else:
        st.warning("Please enter a question.")

st.markdown(
    """
    **Instructions:**
    - Ask a question related to the STUDENT database.
    - The app will generate an SQL query and fetch results from the database.
    - Example questions:
        - "How many students are in Data Science class?"
        - "Show all students with marks above 80."
    """
)
