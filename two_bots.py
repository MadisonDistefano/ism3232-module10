# two_bots.py
# Author: Madison DiStefano

from chatbot import SupportChatbot
from mock_model import MockModel
from order_tool import OrderLookup
from stock_tool import StockLookup

ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

PRODUCTS = {
    "rain jacket": 12,
    "running shoes": 8,
    "water bottle": 20,
}

order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(PRODUCTS)
model = MockModel()

sunny = SupportChatbot(
    "Sunny",
    "You are a friendly support assistant.",
    order_tool,
    stock_tool,
    model,
)

river = SupportChatbot(
    "River",
    "You are a helpful and patient support assistant.",
    order_tool,
    stock_tool,
    model,
)

sunny.respond("hello")
sunny.respond("What is the status of order A100?")

river.respond("hello")

print(f"{sunny.name} history length: {len(sunny.history)}")
print(f"{river.name} history length: {len(river.history)}")

print(f"{sunny.name}'s first reply: {sunny.history[1]['content']}")
print(f"{river.name}'s first reply: {river.history[1]['content']}")

print(f"{sunny.name}'s instructions: {sunny.instructions}")
print(f"{river.name}'s instructions: {river.instructions}")
