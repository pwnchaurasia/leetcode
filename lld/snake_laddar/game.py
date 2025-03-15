from lld.snake_laddar.board import Board
from lld.snake_laddar.dice import Dice
from lld.snake_laddar.player import Player


class Game:
    def __init__(self, players, board_size=100):
        self.players = [Player(name) for name in players]
        self.board = Board(board_size)
        self.dice = Dice()
        self.current_player_index = 0

    def add_snake(self, start, end):
        self.board.add_snake(start, end)

    def add_ladder(self, start, end):
        self.board.add_ladder(start, end)

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"\n{current_player.name}'s turn:")
        input("Press Enter to roll the dice...")
        steps = self.dice.roll()
        self.board.move_player(current_player, steps)

        if self.board.has_won(current_player):
            print(f"\n{current_player.name} has won the game!")
            return True

        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return False

    def start(self):
        print("Starting Snake and Ladder Game!")
        while True:
            if self.play_turn():
                break