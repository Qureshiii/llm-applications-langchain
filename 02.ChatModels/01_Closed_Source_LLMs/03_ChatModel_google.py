from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# 1. Switch to 1.5-flash to bypass the 3.8 rate limit block
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

response = model.invoke('What is the Capital of Spain?')

# 2. Fix the brackets and strip out the double asterisks cleanly
print(response.content[0]['text'].replace("**", ""))

