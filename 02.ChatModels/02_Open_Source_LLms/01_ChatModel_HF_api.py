from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke('What is the capital of Pakistan')

print(result.content)