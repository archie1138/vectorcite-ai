import os
from dotenv import load_dotenv
from langchain.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.4,
    timeout=30,
)

SysMessage = SystemMessage(content="you are a helpful assistant")

message1 = HumanMessage(
    content = "What is RAG ?" 
)

message2 = HumanMessage(
    content = "What is CAD ?" 
)

response = llm.invoke([SysMessage, message1, message2])

print(response.content)