# my_main.py
# Author: Madison DiStefano

from my_assistant import BeautyAssistant
from my_tool import AppointmentLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """
You are Bella, a friendly and helpful beauty salon assistant.

The salon is open Monday through Friday from 9 AM to 6 PM.
Haircuts start at $35.
The salon offers haircuts, hair coloring, and manicures.

Only provide information included in these instructions.
If you do not know an answer, say you do not know and offer to connect
the customer with a salon team member.
Keep your answers short and friendly.
"""

APPOINTMENTS = {
    "Emma": "November 5 at 10:00 AM for a haircut",
    "Olivia": "November 7 at 2:00 PM for a hair color",
    "Sophia": "November 9 at 11:30 AM for a manicure",
}

appointment_tool = AppointmentLookup(APPOINTMENTS)
model = OllamaModel(MODEL_NAME)

bella = BeautyAssistant(
    "Bella",
    INSTRUCTIONS,
    appointment_tool,
    model,
)

print("Bella Beauty Salon Assistant")
print("Type 'quit' to end the conversation.")

while True:
    user_message = input("You: ")

    if user_message.lower() == "quit":
        print("Bella: Thank you for chatting with us. Have a beautiful day!")
        break

    print(f"Bella: {bella.respond(user_message)}")
