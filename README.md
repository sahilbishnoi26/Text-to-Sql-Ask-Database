# Text-to-SQL Query Generator

## Description
This project showcases a Streamlit application that uses AI to convert natural language queries into SQL commands and execute them on a SQLite database. It leverages LangChain and LLMs to streamline database interactions.

## Features
- **Natural Language to SQL**: Converts plain English questions into SQL queries.
- **AI-Powered Query Generator**: Utilizes advanced language models to generate SQL queries.
- **Database Interaction**: Executes generated queries on a SQLite database.
- **Intuitive Interface**: Provides an interactive GUI using Streamlit.
- **Detailed Results**: Displays query results clearly and concisely.

## Technologies Used
- **llama-3.3-70b-versatile**: LLM via Groq API for SQL query generation.
- **LangChain**: For chaining LLMs and prompt templates.
- **Streamlit**: Framework for building the interactive web app.
- **SQLite**: Lightweight database for data storage and retrieval.
- **Python**: Core programming language.

## Installation
1. **Clone the Repository**  
   - `git clone https://github.com/your-username/Text-to-Sql-Ask-Your-Database.git`  
   - `cd Text-to-Sql-Ask-Your-Database`

2. **Create and Activate a Virtual Environment**  
   - On Windows:  
     - `python -m venv venv`  
     - `venv\Scripts\activate`
   - On macOS/Linux:  
     - `python3 -m venv venv`  
     - `source venv/bin/activate`

3. **Install Dependencies**  
   - `pip install -r requirements.txt`

4. **Set Up Environment Variables**  
   - Create a `.env` file in the root directory and add the required API keys. Example:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## Usage
1. **Run the Application**  
   - Start the Streamlit app:
     ```bash
     streamlit run app.py
     ```

2. **Input Your Query**  
   - Enter your natural language question into the input field, e.g., "How many students scored above 90?"

3. **View Results**  
   - The app will display the generated SQL query and fetch the results from the database.
   ![alt text](https://github.com/sahilbishnoi26/Text-to-Sql-Ask-Database/blob/main/text-to-sql.png)

## Troubleshooting
- **Issue**: Missing Dependencies  
  - **Solution**: Ensure all dependencies are installed using `pip install -r requirements.txt`.
- **Issue**: Invalid API Key  
  - **Solution**: Verify your `GROQ_API_KEY` in the `.env` file.
- **Issue**: Database Error  
  - **Solution**: Confirm `student.db` exists and is populated with data. If not then use `student.py` to create a test database
