import os
from langchain.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


def test_llm_returns_nonempty_response() :

    llm = ChatOpenAI(
        model="openai/gpt-oss-120b",
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
        max_completion_tokens=200,
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

    assert response.content is not None
    assert len(response.content) > 0

 