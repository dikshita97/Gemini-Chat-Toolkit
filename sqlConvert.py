# Importing Libraries

from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load Environment Variables and fetch the key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0].format(dbName=prompt_table_name, col_name = col_name),question])
    return response.text

def get_col_name(dbName):
    con=sqlite3.connect("employees.db")
    cur =con.cursor()
    cur.execute("select * from EMPLOYEES limit 1")
    col_name=[i[0] for i in cur.description]
    return col_name

## Fucntion To retrieve query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    Given a SQL database with a table named {dbName} and various columns such as {col_name[0]}, {col_name[1]}, {col_name[2]}, etc., you will translate English questions into corresponding SQL commands.

    For example:
    Example 1: "How many entries are present in the table?", the SQL command will be `SELECT COUNT(*) FROM {dbName};`
    Example 2: "Show me all records where COLUMN_1 is 'Value'", the SQL command will be `SELECT * FROM {dbName} WHERE COLUMN_1 = 'Value';`

    Please note that the SQL code should not include ``` at the beginning or end, and should not contain the word "sql" in the output.
    """
]

# Store DB name entered in the streamlit input
prompt_table_name = ""


# Main Function
def main():
    question = st.text_input("Query Prompt: ",value="Enter the Query",key="input")
    db_name = st.text_input("DB Name: ", value="Enter the Database Name with .db", key="dbName")
    table_name = st.text_input("Table Name: ", value="Enter the Table Name", key="tableName")

    submit=st.button("Ask the question")

    # if submit is clicked
    if submit:
        # Update prompt_db_name with user input
        global prompt_table_name
        prompt_table_name = table_name

        global col_name
        col_name = get_col_name(db_name)
 
        response=get_gemini_response(question,prompt)
        response=read_sql_query(response,db_name)
        st.subheader("The Response is")
        for row in response:
            st.text(row)