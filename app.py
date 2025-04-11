from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure GenAI key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.5-pro-preview-03-25')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query results from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name GOLD_RATE and has the following columns - 
    DATE, CITY, GOLD_TYPE, RATE_PER_GRAM.
    
    For example:
    Example 1 - Show all the gold rates?, 
    the SQL command will be: SELECT * FROM GOLD_RATE;
    
    Example 2 - What is the rate of 24K gold in Mumbai?, 
    the SQL command will be: SELECT RATE_PER_GRAM FROM GOLD_RATE 
    WHERE CITY="Mumbai" AND GOLD_TYPE="24K";
    
    Note: Do not include ``` or the word 'sql' in your output.
    """
]

# Streamlit UI
st.set_page_config(page_title="Gold Rate SQL Query App")
st.header("Gemini App to Retrieve Gold Rate Data")

question = st.text_input("Input:", key="input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print("Generated SQL:", response)
    response = read_sql_query(response, "gold_rate.db")
    st.subheader("The Response is")
    for row in response:
        st.write(row)
    st.success("Query executed successfully!")
else:
    st.warning("Please enter a question and click 'Ask the question' to get started.")
# The above code is a Streamlit application that allows users to ask questions about gold rates.