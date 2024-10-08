# driver.py

from enums import EventType, RecurringType
from lld.meeting_scheduler.calendar import Calendar
from users import User


def main():
    # Create Users
    print("Registering users...")
    customer = User(name="Alice", email="alice@example.com", password="alicepass")
    User.add_user(customer)
    organiser = User(name="Bob", email="bob@example.com", password="bobpass")
    User.add_user(organiser)
    participant1 = User(name="Charlie", email="charlie@example.com", password="charliepass")
    User.add_user(participant1)
    participant2 = User(name="Diana", email="diana@example.com", password="dianapass")
    User.add_user(participant2)

    print("\n All users list...")
    print(User.get_all_users())


    # Create Calendars for Users (already done in User.__init__)
    print("\nCreating calendars...")

    # Organiser adds an event and invites participants
    print("\nOrganiser adding an event...")
    organiser_calendar = organiser.get_my_calendar()
    event = organiser_calendar.add_event(
        event_date="2024-05-01",
        event_time="10:00",
        event_type=EventType.ONCE,
        every=RecurringType.NONE,
        organiser=organiser,
        participants=[participant1, participant2]
    )

    event2 = organiser_calendar.add_event(
        event_date="2025-05-01",
        event_time="11:00",
        event_type=EventType.ONCE,
        every=RecurringType.NONE,
        organiser=organiser,
        participants=[]
    )

    event3 = organiser_calendar.add_event(
        event_date="2026-05-01",
        event_time="11:00",
        event_type=EventType.ONCE,
        every=RecurringType.NONE,
        organiser=organiser,
        participants=[]
    )

    # Participants accept the event
    print("\nParticipants responding to the event...")
    event.accept(participant1)
    event.accept(participant2)

    # Participant1 proposes a new time
    print("\nParticipant1 proposing a new time...")
    event.propose_new_time(participant1, new_date="2024-05-02", new_time="11:00")

    # Organiser confirms the new time (assuming organiser accepts the proposal)
    print("\nOrganiser updating the event with new time...")
    organiser_calendar.remove_event(event)  # Remove the old event
    new_event = organiser_calendar.add_event(
        event_date="2024-05-02",
        event_time="11:00",
        event_type=EventType.ONCE,
        every=RecurringType.NONE,
        organiser=organiser,
        participants=[participant1, participant2]
    )

    # Participant2 rejects the new event
    print("\nParticipant2 rejecting the new event...")
    new_event.reject(participant2)

    # List events for participant1
    print("\nListing events for Participant1 on 2024-05-02...")
    events = Calendar.list_events(user=participant1, date="2024-05-02")
    for e in events:
        print(e)

    # List events for participant2
    print("\nListing events for Participant2 on 2024-05-02...")
    events = Calendar.list_events(user=participant2, date="2024-05-02")
    for e in events:
        print(e)

    # Remove a user
    print("\nRemoving user Diana...")
    User.remove_user(participant2)

    # List all users
    print("\nListing all users:")
    all_users = User.get_all_users()
    for user in all_users:
        print(user)


if __name__ == "__main__":
    main()