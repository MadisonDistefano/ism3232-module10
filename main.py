# main.py
# Author: Madison DiStefano

from chatbot import SupportChatbot
from ollama_model import OllamaModel
from order_tool import OrderLookup
from stock_tool import StockLookup

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """
You are Sunny, a support assistant for Bayside Outfitters.
Answer in one short sentence.
Store hours are 10 am to 7 pm every day.
Returns are accepted within 30 days with a receipt.
Shipping takes 3 to 5 business days.
Sale items cannot be returned.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to a human agent.
"""

ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

STOCK = {
    "rain jacket": 12,
    "day pack": 0,
    "trail hat": 5,
}

order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(STOCK)
model = OllamaModel(MODEL_NAME)

sunny = SupportChatbot(
    "Sunny",
    INSTRUCTIONS,
    order_tool,
    stock_tool,
    model,
)

print("Sunny: Hello! Welcome to Bayside Outfitters. How can I help?")
print("Type 'quit' to end the conversation.")

while True:
    user_message = input("You: ")

    if user_message.lower() == "quit":
        break

    reply = sunny.respond(user_message)
    print(f"Sunny: {reply}")

print(f"Conversation messages: {len(sunny.history)}")
