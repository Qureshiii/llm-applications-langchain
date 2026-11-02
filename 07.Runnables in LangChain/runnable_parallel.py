from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel


# First thing first, loading the environment variables from .env file, do not forget!
load_dotenv()

# Creating the Groq model client. We using 'openai/gpt-oss-20b' model here.
model = ChatGroq(model="openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' :  prompt1 | model | parser ,
    'linkedin' : prompt2 | model | parser
})

result = parallel_chain.invoke({'topic':'AI'})

print("--- TWEET ---")
print(result['tweet'])

print("\n--- LINKEDIN POST ---")
print(result['linkedin'])