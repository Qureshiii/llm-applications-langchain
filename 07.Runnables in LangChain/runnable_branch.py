from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch


# First thing first, loading the environment variables from .env file, do not forget!
load_dotenv()

parser = StrOutputParser()

# Creating the Groq model client. Changed to a valid, supported Groq model identifier.
model = ChatGroq(model="openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template='write a detailed report on \n {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summerize the text \n  {text}',
    input_variables=['text']
)

report_gen_chain = prompt1 | model | parser 

branch_chain = RunnableBranch(
    #(condition, runnable)
    (lambda x:len(x.split())>500, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = report_gen_chain | branch_chain

result = final_chain.invoke({'topic':'Russia Vs Ukraine'})


print("\n" + "="*50)
print("📌 EXECUTING LANGCHAIN ROUTING CHAIN")
print("="*50)
print("\n📝 GENERATED OUTPUT:\n")
print(result)
print("\n" + "="*50)
print("✅ EXECUTION COMPLETED SUCCESSFULLY")
print("="*50 + "\n")