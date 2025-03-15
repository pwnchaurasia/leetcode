from lld.snake_laddar.game import Game

if __name__ == "__main__":
    players = ["p1", "p2"]
    game = Game(players=players)

    # Add snakes
    game.add_snake(16, 6)
    game.add_snake(47, 26)
    game.add_snake(49, 11)
    game.add_snake(56, 53)
    game.add_snake(62, 19)
    game.add_snake(64, 60)
    game.add_snake(87, 24)
    game.add_snake(93, 73)
    game.add_snake(95, 75)
    game.add_snake(98, 78)

    # Add ladders
    game.add_ladder(1, 38)
    game.add_ladder(4, 14)
    game.add_ladder(9, 31)
    game.add_ladder(21, 42)
    game.add_ladder(28, 84)
    game.add_ladder(36, 44)
    game.add_ladder(51, 67)
    game.add_ladder(71, 91)
    game.add_ladder(80, 100)

    # Start the game
    game.start()

