from lld.meeting_scheduler.notification import Notification


class NotificationService:
    @staticmethod
    def notify_organiser(user, message="Message sent to organiser about the event"):
        ## To different methods because we can have different template for organiser and participant
        print("Sending notification to the organiser")
        Notification(user, message).send()

    @staticmethod
    def notify_participants(user, message="Message sent to participants about the event"):
        Notification(user, message).send()