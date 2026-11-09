# echo_model.py
# Author: Madison DiStefano


class EchoModel:
    """A model that repeats the user's last message."""

    def reply(self, instructions, history):
        """Return the last user message."""
        return "You said: " + history[-1]["content"]
