

class Notification:
    def __init__(self, receiver, message):
        self.receiver = receiver  # Could be a user, driver, or admin
        self.message = message

    def send(self):
        # For simplicity, just print the notification (in real life, this could be a push notification)
        print(f"Notification to {self.receiver.name}: {self.message}")