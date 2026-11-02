class BeautyAssistant:
    """A mock beauty salon assistant named Bella."""

    def __init__(self, name, instructions, appointment_tool):
        self.name = name
        self.instructions = instructions
        self.appointment_tool = appointment_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})

        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()

        if any(word in text for word in ["book", "schedule", "reschedule", "cancel"]):
            return (
                "I'd be happy to help! I'll connect you with a salon team "
                "member to handle your appointment request."
            )

        if "appointment" in text:
            return self.appointment_reply(user_message)

        if "hello" in text or "hi" in text:
            return (
                f"Hello! I'm {self.name}, your beauty salon assistant. "
                "How can I help you today?"
            )

        return (
            "I can help check an existing appointment or connect you "
            "with a salon team member."
        )

    def appointment_reply(self, user_message):
        client = self.appointment_tool.find_client(user_message)

        if client is None:
            return (
                "I couldn't identify the client name. "
                "Please provide the name on the appointment."
            )

        appointment = self.appointment_tool.find_appointment(client)

        if appointment is None:
            return f"I couldn't find an appointment for {client}."

        return f"{client}'s appointment is: {appointment}."
