from collections import defaultdict


class Board:
    def __init__(self, size=100):
        self.size = size
        self.snakes = {}  # key: start, value: end
        self.ladders = {}  # key: start, value: end
        self.player_positions = defaultdict(int)  # player_name: position

    def add_snake(self, start, end):
        if self.size >= start > end >= 1:
            self.snakes[start] = end
        else:
            raise ValueError("Invalid snake position")

    def add_ladder(self, start, end):
        if 1 <= start < end <= self.size:
            self.ladders[start] = end
        else:
            raise ValueError("Invalid ladder position")

    def move_player(self, player, steps):
        new_position = player.move(steps)
        if new_position > self.size:
            print(f"{player.name} cannot move beyond the board. Staying at {player.position - steps}")
            player.position -= steps
            return

        print(f"{player.name} rolled a {steps} and moved from {player.position - steps} to {new_position}")

        # Check for snakes
        if new_position in self.snakes:
            print(f"Oops! {player.name} got bitten by a snake at {new_position}")
            player.position = self.snakes[new_position]
            print(f"{player.name} is now at {player.position}")

        # Check for ladders
        if new_position in self.ladders:
            print(f"Yay! {player.name} climbed a ladder at {new_position}")
            player.position = self.ladders[new_position]
            print(f"{player.name} is now at {player.position}")

    def has_won(self, player):
        return player.position == self.size