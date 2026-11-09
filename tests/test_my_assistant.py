# tests/test_my_assistant.py
# Author: Madison DiStefano

from mock_model import MockModel
from my_assistant import BeautyAssistant
from my_tool import AppointmentLookup


class SilentModel:
    """A model that does not return an answer."""

    def reply(self, instructions, history):
        return None


def make_assistant(model=None):
    appointments = {
        "Emma": "November 5 at 10:00 AM for a haircut",
        "Olivia": "November 7 at 2:00 PM for a hair color",
        "Sophia": "November 9 at 11:30 AM for a manicure",
    }

    if model is None:
        model = MockModel()

    return BeautyAssistant(
        "Bella",
        "You are a friendly beauty salon assistant.",
        AppointmentLookup(appointments),
        model,
    )


def test_hello_reply():
    bella = make_assistant()
    assert "Hello!" in bella.respond("hello")


def test_appointment_lookup():
    bella = make_assistant()
    reply = bella.respond("What is Emma's appointment?")
    assert "November 5" in reply


def test_unknown_client():
    bella = make_assistant()
    reply = bella.respond("What is John's appointment?")
    assert "couldn't find" in reply


def test_booking_request_connects_to_team_member():
    bella = make_assistant()
    reply = bella.respond("I want to book an appointment")
    assert "connect you with a salon team member" in reply


def test_history_records_messages():
    bella = make_assistant()
    bella.respond("hello")
    assert len(bella.history) == 2
    assert bella.history[0]["role"] == "user"
    assert bella.history[1]["role"] == "assistant"


def test_other_questions_use_model():
    bella = make_assistant()
    reply = bella.respond("Tell me a joke")
    assert "not sure" in reply


def test_safe_reply_when_model_returns_none():
    bella = make_assistant(SilentModel())
    reply = bella.respond("Tell me a joke")
    assert "connect you" in reply
