import os
import sqlite3
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Function to convert user input into SQL query
def get_sql_query(user_query):
    """
    Convert a natural language question into a SQL query using the ChatGroq model.

    Args:
        user_query (str): User's question in natural language.

    Returns:
        str: Generated SQL query.
    """
    # Define the system prompt for the LLM
    groq_sys_prompt = ChatPromptTemplate.from_template("""
                    You are an expert in converting English questions to SQL query!
                    The SQL database has the name STUDENT and has the following columns - NAME, COURSE, 
                    SECTION and MARKS. For example, 
                    Example 1 - How many entries of records are present?, 
                        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
                    Example 2 - Tell me all the students studying in Data Science COURSE?, 
                        the SQL command will be something like this SELECT * FROM STUDENT 
                        where COURSE="Data Science"; 
                    Also, the SQL code should not have ``` in the beginning or end and no "sql" word 
                    in the output.
                    Now convert the following question in English to a valid SQL Query: {user_query}. 
                    No preamble, only valid SQL please.
                    """)
    
    # Define the model to use
    model = "llama3-8b-8192"
    llm = ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name=model
    )

    # Create the transformation chain
    chain = groq_sys_prompt | llm | StrOutputParser()
    response = chain.invoke({"user_query": user_query})
    return response


# Function to execute the SQL query and return results
def return_sql_response(sql_query):
    """
    Execute the SQL query on the STUDENT database and fetch results.

    Args:
        sql_query (str): The SQL query to execute.

    Returns:
        list: List of rows fetched from the database.
    """
    database = "student.db"
    with sqlite3.connect(database) as conn:
        return conn.execute(sql_query).fetchall()


# Main Streamlit app
def main():
    """
    Main function to render the Streamlit app for converting text to SQL and querying the database.
    """
    # Set up Streamlit app configuration
    st.set_page_config(page_title="Text To SQL", page_icon="📊", layout="wide")

    # App title and description
    st.title("Text to SQL Query Generator 🛠️")
    st.markdown("""
    **Welcome to the Text-to-SQL Query Generator!**
    This app allows you to ask questions in plain English and automatically converts them into SQL queries to interact with your database.
    """)

    # Input section for user's query
    st.sidebar.header("Query Input")
    user_query = st.sidebar.text_input("Type your question here:", placeholder="E.g., How many students scored above 80?")

    # Button to submit the query
    if st.sidebar.button("Submit Query"):
        if user_query.strip():
            with st.spinner("Processing your query..."):
                try:
                    # Generate SQL query
                    sql_query = get_sql_query(user_query)

                    # Fetch results from the database
                    retrieved_data = return_sql_response(sql_query)

                    # Display SQL query and results
                    st.success("SQL Query Successfully Generated!")
                    st.code(sql_query, language="sql")
                    st.subheader("Query Results:")
                    if retrieved_data:
                        for row in retrieved_data:
                            st.write(row)
                    else:
                        st.warning("No data found for the given query.")

                except Exception as e:
                    # Handle errors (e.g., invalid queries)
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid query.")


if __name__ == '__main__':
    main()
