class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps
        return self.position

    def __str__(self):
        return f"{self.name} is at position {self.position}"