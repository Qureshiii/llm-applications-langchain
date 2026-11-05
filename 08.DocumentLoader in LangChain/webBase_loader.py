from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'

loader = WebBaseLoader(url)

docs = loader.load()


# First thing first, loading the environment variables from .env file, do not forget!
load_dotenv()

parser = StrOutputParser()

# Creating the Groq model client. Changed to a valid, supported Groq model identifier.
model = ChatGroq(model="openai/gpt-oss-20b")

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text -  \n {text}',
    input_variables=['question', 'text']
)


docs = loader.load()


chain = prompt | model | parser

response = chain.invoke({'question':'what is the product that we are talking about?', 'text':docs[0].page_content})

print(response)