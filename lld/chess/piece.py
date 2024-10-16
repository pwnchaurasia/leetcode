import abc

class Piece(metaclass=abc.ABCMeta):
    def __init__(self, color):
        self.color = color
        self.name = str(self.__class__.__name__)

    @abc.abstractmethod
    def valid_move(self, position_x, position_y):
        pass

    def __repr__(self):
        return f"{self.color}_{self.name}"


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_move(self, position_x, position_y):
        pass


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_move(self, position_x, position_y):
        pass

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_move(self, position_x, position_y):
        pass


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_move(self, position_x, position_y):
        pass

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_move(self, position_x, position_y):
        pass


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_move(self, position_x, position_y):
        pass