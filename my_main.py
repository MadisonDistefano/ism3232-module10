from my_assistant import BeautyAssistant
from my_tool import AppointmentLookup

APPOINTMENTS = {
    "Emma": "November 5 at 10:00 AM for a haircut",
    "Olivia": "November 7 at 2:00 PM for a hair color",
    "Sophia": "November 9 at 11:30 AM for a manicure",
}

appointment_tool = AppointmentLookup(APPOINTMENTS)

bella = BeautyAssistant(
    "Bella",
    "You are a friendly and helpful beauty salon assistant.",
    appointment_tool,
)

print("Bella Beauty Salon Assistant")
print("Type 'quit' to end the conversation.")

while True:
    user_message = input("You: ")

    if user_message.lower() == "quit":
        print("Bella: Thank you for chatting with us. Have a beautiful day!")
        break

    print(f"Bella: {bella.respond(user_message)}")
