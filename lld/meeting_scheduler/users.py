from lld.meeting_scheduler.calendar import Calendar


class User:
    _users = []

    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password
        self._calendar = Calendar(user=self)

    def get_my_calendar(self):
        return self._calendar

    @classmethod
    def add_user(cls, user):
        cls._users.append(user)
        print("user added successfully")
        return True

    @classmethod
    def remove_user(cls, user):
        if user in cls._users:
            cls._users.remove(user)
            print("user removed successfully")

    @classmethod
    def get_all_users(cls):
        return cls._users

    @property
    def name(self):
        return self._name


    @property
    def email(self):
        return self._email

    def __repr__(self):
        return f"User(name={self._name}, email={self._email})"