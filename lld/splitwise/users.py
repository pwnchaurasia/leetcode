class User:
    users = []

    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.friends = []
        self.groups = []
        self.balance = 0

    def add(self):
        User.users.append(self)

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            friend.friends.append(self)  # Ensures bidirectional friendship

    def total_balance(self):
        print(f"{self} balance is {self.balance}")
        return self.balance

    def __repr__(self):
        return f"User({self.name}, {self.email})"