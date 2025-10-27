"""Utility function to call the OpenAI LLM API."""
import os
from openai import OpenAI

def call_llm(messages):
    """Call the OpenAI LLM with the provided messages."""
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key"))

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content
