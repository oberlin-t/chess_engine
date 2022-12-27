class Piece:
    def __init__(self, name, position, is_white):
        self.name = name
        self.position = position
        self.is_white = is_white

    def __repr__(self):
        if self.is_white:
            return self.name
        return self.name.lower()

class King(Piece):
    def __init__(self, position, is_white):
        super().__init__("K", position, is_white)
        self.moved = False

    def possible_moves(self, board):
        return 0

class Pawn(Piece):
    def __init__(self, position, is_white):
        super().__init__("P", position, is_white)
        self.moved = False
        self.passantable = False

    def possible_moves(self, board):
        return 0

class Rook(Piece):
    def __init__(self, position, is_white):
        super().__init__("R", position, is_white)
        self.moved = False

    def possible_moves(self, board):
        return 0


class Knight(Piece):
    def __init__(self, position, is_white):
        super().__init__("N", position, is_white)

    def possible_moves(self, board):
        return 0

class Bishop(Piece):
    def __init__(self, position, is_white):
        super().__init__("B", position, is_white)

    def possible_moves(self, board):
        return 0

class Queen(Piece):
    def __init__(self, position, is_white):
        super().__init__("Q", position, is_white)

    def possible_moves(self, board):
        return 0


