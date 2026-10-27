"""
Sentiment Analysis Tool using LangChain and Groq.

This module sets up a structured LLM chain that classifies the sentiment 
of user feedback into 'positive' or 'negative' using a Pydantic output parser 
for type-safe data extraction.
"""
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

# First thing first, loading the environment variables from .env file, do not forget!
load_dotenv()

# Creating the Groq model client. We using 'openai/gpt-oss-20b' model here.
model = ChatGroq(model="openai/gpt-oss-20b")

# Simple string parser for catching the text, standard helper.
parser1 = StrOutputParser()

class Feedback(BaseModel):
    """
    Data validation schema defining the structured fields required from the model output.
    """
    # Setting up the strict choices, model must select only 'positive' or 'negative'.
    sentiment : Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

# Making the Pydantic parser, it will force the model to give nice JSON structure.
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Making the main prompt, also injecting the special format instructions here.
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

# Binding prompt, model, and parser together using modern LCEL chain. Very clean!
classifier_chain = prompt1 | model | parser2

# Prompt for writing nice reply when feedback is positive.
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

# Prompt for writing nice reply when feedback is negative.
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Conditional routing branch. Checking the sentiment inside Pydantic output and routing accordingly.
brach_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser1),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)

# Combining classification chain and branching chain together into one big master chain!
chain = classifier_chain | brach_chain

# Finally, invoking the complete chain with our sample sentence to see the magic.
result = chain.invoke({"feedback":"This is a wonderful smartphone"})


# Printing the final output response on the screen.
# print(result)

chain.get_graph().print_ascii()