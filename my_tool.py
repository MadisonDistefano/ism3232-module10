class AppointmentLookup:
    """A mock tool for looking up beauty salon appointments."""

    def __init__(self, appointments):
        self.appointments = appointments

    def find_client(self, text):
        text = text.lower()

        for client in self.appointments:
            if client.lower() in text:
                return client

        return None

    def find_appointment(self, client):
        return self.appointments.get(client)
