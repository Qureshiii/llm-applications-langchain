import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

# --- FIRST STEP: Generate Report ---
prompt1 = template1.invoke({'topic': 'Black hole'})
# Direct text standard use (model.invoke string return karega)
result1 = model.invoke(prompt1)

# --- SECOND STEP: Generate Summary ---
prompt2 = template2.invoke({'text': result1}) # prompt2 pass string content directly
result2 = model.invoke(prompt2)

# Output print karein
print(result2.content)
