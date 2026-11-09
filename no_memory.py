# no_memory.py
# Author: Madison DiStefano

from ollama import chat

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = "You are a helpful assistant."

first_response = chat(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": INSTRUCTIONS},
        {"role": "user", "content": "Hello, my name is Dana."},
    ],
)

print(first_response.message.content)

second_response = chat(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": INSTRUCTIONS},
        {"role": "user", "content": "What is my name?"},
    ],
)

print(second_response.message.content)
