
from lld.meeting_scheduler.enums import EventStatus, EventType, RecurringType
from lld.meeting_scheduler.notification_service import NotificationService


class Event:
    def __init__(self,
                 calendar,
                 event_date,
                 event_time,
                 event_type=EventType.ONCE,
                 every=RecurringType.NONE,
                 organiser=None,
                 participants=None):
        self._calendar = calendar
        self._event_date = event_date
        self._event_time = event_time
        self._status = EventStatus.SCHEDULED
        self._event_type = event_type
        self._participants = participants if participants else []
        self._organiser = organiser if organiser else calendar.user
        self._every = every
        self.validate()

    def validate(self):
        print(f"Validated data {self}")
        return self

    @property
    def event_date(self):
        return self._event_date

    def notify(self):
        NotificationService.notify_organiser(
            user=self._organiser,
            message=f"Added event for date {self.event_date} time {self._event_time}")

        for participant in self._participants:
            NotificationService.notify_participants(user=participant,
                                                    message=f"User {self._organiser} added event for date "
                                                            f"{self.event_date} time {self._event_time}")
        print("Notification sent")

    def accept(self, participant):
        from lld.meeting_scheduler.calendar import Calendar
        if participant not in self._participants:
            print(f"{participant.name} is not a participant of this event.")
            return False
            # Assuming accept means adding to their calendar
        participant_calendar = Calendar.get_user_calendar(participant)
        participant_calendar.add_event(
            event_date=self._event_date,
            event_time=self._event_time,
            event_type=self._event_type,
            every=self._every,
            organiser=self._organiser,
            participants=[participant]
        )
        print(f"{participant.name} accepted the event.")
        return True

    def reject(self, participant):
        if participant not in self._participants:
            print(f"{participant.name} is not a participant of this event.")
            return False
        self._participants.remove(participant)
        print(f"{participant.name} rejected the event.")
        if not self._participants:
            self.cancel_event()
        return True

    def propose_new_time(self, participant, new_date, new_time):
        if participant not in self._participants:
            print(f"{participant.name} is not a participant of this event.")
            return False
        # Notify organiser about the proposal
        NotificationService.notify_organiser(
            user=self._organiser,
            message=f"User {participant.name} has proposed a new time for the event: {new_date} at {new_time}"
        )
        print(f"{participant.name} proposed a new time: {new_date} at {new_time}")
        # You can store proposed times if needed
        return True

    def cancel_event(self):
        self._status = EventStatus.CANCELLED
        NotificationService.notify_organiser(
            user=self._organiser,
            message=f"The event on {self._event_date} at {self._event_time} has been cancelled."
        )
        for participant in self._participants:
            NotificationService.notify_participants(
                user=participant,
                message=f"The event on {self._event_date} at {self._event_time} has been cancelled."
            )
        print("Event cancelled due to no participants.")