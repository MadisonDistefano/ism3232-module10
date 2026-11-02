from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup


def make_bot():
    orders = {"A100": "shipped", "A101": "processing"}
    products = {"rain jacket": 12, "running shoes": 8}

    return SupportChatbot(
        "Sunny",
        "Be friendly.",
        OrderLookup(orders),
        StockLookup(products),
    )


def test_hello_reply():
    bot = make_bot()
    assert "Hello!" in bot.respond("hello")


def test_order_question_uses_tool():
    bot = make_bot()
    assert bot.respond("What is the status of order A100?") == (
        "Order A100 is shipped."
    )


def test_order_question_without_id():
    bot = make_bot()
    assert "Which order?" in bot.respond("Can you check my order?")


def test_handoff_for_payment():
    bot = make_bot()
    assert "human agent" in bot.respond("I need help with payment")


def test_fallback_reply():
    bot = make_bot()
    assert "not sure" in bot.respond("Tell me a joke")


def test_history_records_user_and_assistant():
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_needs_human():
    bot = make_bot()
    assert bot.needs_human("I need help with my card") is True


def test_count_user_messages():
    bot = make_bot()
    bot.respond("hello")
    bot.respond("What is the status of order A100?")
    assert bot.count_user_messages() == 2


def test_stock_question_uses_tool():
    bot = make_bot()
    assert bot.respond("Is the rain jacket in stock?") == (
        "We have 12 of the rain jacket in stock."
    )


def test_stock_question_for_unknown_product():
    bot = make_bot()
    assert "Which product?" in bot.respond("Is the backpack in stock?")
