from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


# First thing first, loading the environment variables from .env file, do not forget!
load_dotenv()

# Creating the Groq model client. We using 'openai/gpt-oss-20b' model here.
model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7)

prompt = PromptTemplate(
    input_variables=['topic'],
    template='Write a joke about topic {topic}.'
)
prompt1 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt | model | parser | prompt1 | model | parser)

print(chain.invoke({'topic':'AI'}))
