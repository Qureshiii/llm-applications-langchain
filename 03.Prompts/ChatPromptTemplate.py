from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

chat_template = ChatPromptTemplate([
    ("system","You are a helpful {domain} expert"),
    ("human","Explain in simple terms, what is {topic}")
    
])

prompt = chat_template.invoke({'domain':'Cricket', 'topic':'Dusra'})

print(prompt)