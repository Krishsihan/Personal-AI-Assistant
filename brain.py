from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def think(user_input, memory):
    prompt = f"""
You are a personal AI assistant.
User memory: {memory}
User says: {user_input}
Think step by step and decide what to do.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
