

class User:
    USERS = {}

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def create_user(self):
        user_exist =  self.USERS.get(self.phone, False)
        if user_exist:
            print("User already exists with this phone number")
            return False

        self.USERS[self.phone] = self
        print("User created")

    def user_update(self):
        pass