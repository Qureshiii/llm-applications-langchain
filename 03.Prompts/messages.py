from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq  # Groq model ko import kiya

load_dotenv()

# Model variable ko initialize kiya (Llama 3.3 model ke sath)
model = ChatGroq(model="openai/gpt-oss-20b")

messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

for msg in messages:
    print(f"{msg.__class__.__name__}: {msg.content}")
    print("-" * 40)

