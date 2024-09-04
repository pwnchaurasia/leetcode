class Player:
    def __init__(self, name, marker) -> None:
        self.name = name
        self.marker = marker


class Board:
    def __init__(self, size) -> None:
        self.reset(size)
        self.size = size
    
    def reset(self, size):
        self.board = [["" for x in range(size)].copy() for y in range(size)]
        self.rowCounts = {}
        self.colCounts = {}
        self.diagCounts = {}
        self.size = size
    
    def print_board(self):
        for i in range(self.size):
            # Print each row of the matrix
            print(' | '.join(self.board[i]))
            # Print a separator line
            if i < self.size - 1:
                print('-' * (self.size * 4 - 3))
    
    def place(self, player, x, y):
        marker = player.marker

        if self.board[x][y] != '':
            raise ValueError
        else:
            self.board[x][y] = marker

            self.rowCounts[x] = self.rowCounts.get(x, {})
            self.rowCounts[x][marker] = self.rowCounts[x].get(marker, 0) + 1

            if self.rowCounts[x][marker] == self.size:
                return True
            
            self.colCounts[y] = self.colCounts.get(y, {})
            self.colCounts[y][marker] = self.colCounts[y].get(marker, 0) + 1

            if self.colCounts[y][marker] == self.size:
                return True
            
            if x == y:
                self.diagCounts["forwards"] = self.diagCounts.get("forwards", {})
                self.diagCounts["forwards"][marker] = self.diagCounts.get("forwards").get(marker, 0) + 1

                if self.diagCounts["forwards"][marker] == self.size:
                    return True


            if x + y == self.size - 1:
                self.diagCounts["backwards"] = self.diagCounts.get("backwards", {})
                self.diagCounts["backwards"][marker] = self.diagCounts.get("backwards").get(marker, 0) + 1

                if self.diagCounts["backwards"][marker] == self.size:
                    return True

            print(self.rowCounts)
            print(self.colCounts)
            print(self.diagCounts)
            return False

class Game:
    def __init__(self, player1, player2, board) -> None:
        self.board = board
        self.player1 = player1
        self.player2 = player2
    
    def playGame(self):
        currTurn = 1
        gameDone = False
        while not gameDone:
            self.board.print_board()
            currPlayer = self.player1 if currTurn %2 == 1 else self.player2
            x = int(input(f"{currPlayer.name } Write X position of marker (row) "))
            y = int(input(f"{currPlayer.name } Write Y position of marker (column) "))
            if self.board.place(currPlayer, x, y):
                gameDone = True
                print(f" {currPlayer.name} wins!! ")
            else:
                currTurn +=1
        



if __name__ == "__main__":
    j = Player("J", "x")
    m = Player("M", "o")

    board = Board(3)

    game  = Game(j, m, board)
    game.playGame()