from my_assistant import BeautyAssistant
from my_tool import AppointmentLookup


def make_assistant():
    appointments = {
        "Emma": "November 5 at 10:00 AM for a haircut",
        "Olivia": "November 7 at 2:00 PM for a hair color",
    }

    tool = AppointmentLookup(appointments)

    return BeautyAssistant(
        "Bella",
        "Be friendly and helpful.",
        tool,
    )


def test_hello_reply():
    bella = make_assistant()
    assert "Hello!" in bella.respond("hello")


def test_existing_appointment():
    bella = make_assistant()
    reply = bella.respond("Can you check Emma's appointment?")
    assert "November 5" in reply


def test_missing_client_name():
    bella = make_assistant()
    reply = bella.respond("Check my appointment")
    assert "couldn't identify" in reply


def test_booking_request_handoff():
    bella = make_assistant()
    reply = bella.respond("I want to book an appointment")
    assert "connect you with a salon team member" in reply


def test_history_records_messages():
    bella = make_assistant()
    bella.respond("hello")
    assert len(bella.history) == 2
    assert bella.history[0]["role"] == "user"
    assert bella.history[1]["role"] == "assistant"
