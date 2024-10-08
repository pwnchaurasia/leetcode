from lld.meeting_scheduler.events import Event


class Calendar:
    _calendars = {}

    def __new__(cls, user):
        if user not in cls._calendars:
            # Create a new instance if the user doesn't already have a calendar
            instance = super(Calendar, cls).__new__(cls)
            cls._calendars[user] = instance
        return cls._calendars[user]

    def __init__(self, user):
        if not hasattr(self, 'initialized'):  # Ensure __init__ is called only once per instance
            self._user = user
            self._events = []
            self.initialized = True  # Mark as initialized

    @classmethod
    def get_user_calendar(cls, user):
        """Returns the calendar of the specified user"""
        return cls._calendars.get(user, None)

    @classmethod
    def remove_calendar(cls, cal):
        if cal in cls._calendars:
            cls._calendars.remove(cal)
            print("Calendar removed successfully")
            return True
        print("Calendar not found")
        return False

    def add_event(self, event_date, event_time, event_type, every, organiser=None, participants=None):
        if participants is None:
            participants = []
        event = Event(calendar=self, event_date=event_date,
                      event_time=event_time, event_type=event_type,
                      every=every, organiser=organiser, participants=participants)
        if event.validate():
            self._events.append(event)
            event.notify()
            print("Event added to calendar")
            return event
        else:
            print("Event validation failed")
            return None

    @classmethod
    def list_events(cls, user, date):
        events = []
        user_calendars = Calendar.get_user_calendar(user)
        events = user_calendars.get_events()
        events = [event for event in events if event.event_date == date]
        if not events:
            print(f"There are no events for user {user} on date: {date}")
        return events

    def remove_event(self, event):
        self._events.remove(event)


    def get_events(self):
        return self._events

    @property
    def user(self):
        return self._user

    def __repr__(self):
        return f"Calendar(user={self._user.name})"
