import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        {'role' : 'system', 'content' : 'you are a helpful assistant.'},
        {'role' : 'user', 'content':'what is RAG, why it is useful?'}
    ],
    max_completion_tokens=200,
    temperature=0.8,
)

print(response.choices[0].message.content)

usage = response.usage

cost = ((0.15*usage.prompt_tokens) + (0.6*usage.completion_tokens))/1000000 

print(f"Total no of input tokens : {usage.prompt_tokens}" )
print(f"Total no of completion tokens : {usage.completion_tokens}" )
print(f"Total no of total tokens : {usage.total_tokens}" )
print(f"Total cost : {cost}" )