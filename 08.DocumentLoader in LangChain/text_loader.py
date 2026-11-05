from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

loader = TextLoader('cricket.txt', encoding='utf-8')

# First thing first, loading the environment variables from .env file, do not forget!
load_dotenv()

parser = StrOutputParser()

# Creating the Groq model client. Changed to a valid, supported Groq model identifier.
model = ChatGroq(model="openai/gpt-oss-20b")

prompt = PromptTemplate(
    template='Write a summary about the following poem - \n {poem}',
    input_variables=['poem']
)


docs = loader.load()


chain = prompt | model | parser

response = chain.invoke({'poem':docs[0].page_content})

print(response)