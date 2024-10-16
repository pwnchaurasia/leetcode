from copy import deepcopy

from lld.chess.piece import Pawn, King, Queen, Rook, Bishop, Knight


class ChessBoard:
    def __init__(self):
        self.board = self.create_board()
        self.display_board()
        self.fill_pieces()
        self.display_board()

    def create_board(self):
        """
        chess board is a matrix of 8x8
        where alternate block is white and black
        :return: matrix of 8x8
        """
        matrix = []
        strip = ["w", "b", "w", "b", "w", "b", "w", "b"]
        for i in range(1, 9):
            strip = deepcopy(strip)
            if i % 2 != 0:
                matrix.append(strip)
            else:
                matrix.append(strip[::-1])
        return matrix

    def display_board(self):
        print("***"*10)
        for i in self.board:
            print(i)
        print("***" * 10)

    def fill_pieces(self):
        # Fill white pieces
        for i in range(8):
            self.board[1][i] = Pawn('white')  # White pawns
        self.board[0][0] = Rook('white')
        self.board[0][1] = Knight('white')
        self.board[0][2] = Bishop('white')
        self.board[0][3] = Queen('white')
        self.board[0][4] = King('white')
        self.board[0][5] = Bishop('white')
        self.board[0][6] = Knight('white')
        self.board[0][7] = Rook('white')

        # Fill black pieces
        for i in range(8):
            self.board[6][i] = Pawn('black')  # Black pawns
        self.board[7][0] = Rook('black')
        self.board[7][1] = Knight('black')
        self.board[7][2] = Bishop('black')
        self.board[7][3] = Queen('black')
        self.board[7][4] = King('black')
        self.board[7][5] = Bishop('black')
        self.board[7][6] = Knight('black')
        self.board[7][7] = Rook('black')



