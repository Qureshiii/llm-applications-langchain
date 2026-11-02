from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough


# First thing first, loading the environment variables from .env file, do not forget!
load_dotenv()

# Creating the Groq model client. Changed to a valid, supported Groq model identifier.
model = ChatGroq(model="openai/gpt-oss-20b")

prompt = PromptTemplate(
    input_variables=['topic'],
    template='Write a joke about topic {topic}.'
)
prompt1 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

parser = StrOutputParser()

joke_gen_chain = prompt | model | parser 

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    # FIX: prompt1 expects a dictionary key called 'text'. 
    # We must format the incoming string from joke_gen_chain into {'text': joke_string}
    'explaination' : {"text": RunnablePassthrough()} | prompt1 | model | parser 
})

final_chain = joke_gen_chain | parallel_chain

result = final_chain.invoke({'topic':'cricket'})

# Clean formatting for the output terminal
print("=" * 40)
print(f"🃏 JOKE:")
print("=" * 40)
print(result['joke'])
print("\n" + "=" * 40)
print(f"🧠 EXPLANATION:")
print("=" * 40)
print(result['explaination'])
print("=" * 40)
