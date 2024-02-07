import sqlite3
import streamlit as st

import google.generativeai as genai
from api import api

genai.configure(api_key=api)

def get_gemini_model(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    return response.text



def get_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    for rows in data:
        print(rows)
    return data


prompt= """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEE and has the following columns - NAME, DEPARTMENT, 
    SALARY \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEE ;
    \nExample 2 - Tell me all the employees  in Data Science department?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    where DEPARTMENT="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """


st.set_page_config(page_title ='SQL LLM QUERY')
st.header('GEMINI PRO FROM TEXT TO QUERY')

question =st.text_input("INPUT: ",key="input")

submit = st.button("Submit to get answer")

if submit:
    response = get_gemini_model(question,prompt)
    responsesql = get_sql_query(response,"TEST.db")
    st.subheader("The response is")
    st.header(responsesql)

    st.subheader("The query is")
    st.header(str(response))
