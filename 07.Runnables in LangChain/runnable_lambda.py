from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda


# First thing first, loading the environment variables from .env file, do not forget!
load_dotenv()

parser = StrOutputParser()

# Creating the Groq model client. Changed to a valid, supported Groq model identifier.
model = ChatGroq(model="openai/gpt-oss-20b")

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

prompt = PromptTemplate(
    input_variables=['topic'],
    template='Write a joke about topic {topic}.'
)



joke_gen_chain = prompt | model | parser 

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)
})

final_chain = joke_gen_chain | parallel_chain

result = final_chain.invoke({'topic':'AI'})

# Clean formatting for the final output terminal
print("\n" + "=" * 40)
print("🃏 JOKE")
print("=" * 40)

# Extract the joke and clean up markdown asterisks (**neural** -> neural)
clean_joke = result['joke'].replace("**", "").replace("*", "").strip()
print(clean_joke)

# If your dictionary contains a word count, print it cleanly at the bottom
if 'word_count' in result:
    print("-" * 40)
    print(f"📊 Word Count: {result['word_count']}")




