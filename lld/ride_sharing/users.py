import hashlib

from lld.ride_sharing.enums import UserType


class User:
    users = {}
    def __init__(self, name, email, password, long, lat, user_type=UserType.RIDER):
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type
        self.long = long
        self.lat = lat

    @staticmethod
    def hashed_password(password):
        md5 = hashlib.md5(password.encode()).hexdigest()
        return md5

    def create_new_user(self):
        self.users[self.email] = {
            "name": self.name,
            "email": self.email,
            "password": User.hashed_password(self.password),
            "user_type": self.user_type,
            "location": self.location
        }
        return self.users[self.email]

    def update_location(self, long, lat):
        self.users[self.email]['long'] = long
        self.users[self.email]['lat'] = lat
