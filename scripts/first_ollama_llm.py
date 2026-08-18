import os
from langchain.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.1",
    temperature=0.4,
)

response = model.invoke([SystemMessage(content="you are a helpful assistant"), HumanMessage(content="What is RAG, and why is it useful?")])

print(response.content)
print(response.usage_metadata)