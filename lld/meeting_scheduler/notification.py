
class Notification:
    def __init__(self, receiver, message):
        self._receiver = receiver
        self._message = message

    def send(self):
        print(f"Sent notification to {self._receiver}")