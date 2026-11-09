# with_memory.py
# Author: Madison DiStefano

from ollama import chat

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = "You are a helpful assistant."

messages = [
    {"role": "system", "content": INSTRUCTIONS},
]

messages.append({"role": "user", "content": "Hello, my name is Dana."})

first_response = chat(model=MODEL_NAME, messages=messages)

messages.append({"role": "assistant", "content": first_response.message.content})

print(first_response.message.content)

messages.append({"role": "user", "content": "What is my name?"})

second_response = chat(model=MODEL_NAME, messages=messages)

messages.append({"role": "assistant", "content": second_response.message.content})

print(second_response.message.content)

print(f"Number of messages: {len(messages)}")
