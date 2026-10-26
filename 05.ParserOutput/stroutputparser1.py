from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# .env file se API keys ko load karein
load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

# 1st prompt template "Detailed report"
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt template "summary" 
template2 = PromptTemplate(
    template='write a 5 lines summary on the following text.\n\n{text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | {"text": RunnablePassthrough()} | template2 | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)