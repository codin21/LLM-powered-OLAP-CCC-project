from dotenv import load_dotenv
import openai
import os
import langchain.llms as llms
#from langchain.chat_models import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.llms import HuggingFaceHub
import pandas as pd
import sqlite3
from langchain_community.utilities import SQLDatabase
from langchain.prompts import PromptTemplate
load_dotenv()
import openpyxl

llm = HuggingFaceHub(repo_id="openai-community/gpt2-medium")
db = SQLDatabase.from_uri("sqlite:///dataset.db")

prompt_template = PromptTemplate(
    input_variables=["input", "top_k", "table_info"],
    template="Generate a SQL query to answer this question: {input}. Using the table info: {table_info}, provide up to {top_k} SQL variations."
)

chain = create_sql_query_chain(prompt=prompt_template, llm=llm, db=db)

response = chain.invoke({"question": "Give me top 3 rows from models table", "top_k": 5}) 

print(response)

# chain = create_sql_query_chain(llm,db)
# response = chain.invoke({"question": "How many records are there in models table"})
# response