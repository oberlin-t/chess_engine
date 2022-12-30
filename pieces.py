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
        moves_list = list()
        if self.is_white == True:
            if board_variable[self.position[0] + 1][self.position[1]] == 0:
                moves_list.append(self.position[0] + 1, self.position[1])

                if self.moved == False and board_variable(self.position[0] + 2) == 0:
                    moves_list.append(self.position[0] + 2, self.position[1])
            
            if self.position[1] + 1 <= 7:
                if board_variable[self.position[0] + 1][self.position[1] + 1] != 0:
                    if board_variable[self.position[0] + 1][self.position[1] + 1].is_white == False:
                        moves_list.append(self.position[0] + 1, self.position[1] + 1)

                if board_variable[self.position[0]][[self.position[1] + 1]] != 0:
                    if board_variable[self.position[0]][[self.position[1] + 1]].name == "P" and board_variable[self.position[0]][self.position[1] + 1].is_white == False:
                        if board_variable[self.position[0]][[self.position[1] + 1]].passantable == True:
                            moves_list.append(self.position[0], self.position[1] + 1)

            if self.position[1] - 1 <= 0:
                if board_variable[self.position[0] + 1][self.position[1] - 1] != 0:
                    if board_variable[self.position[0] + 1][self.position[1] - 1].is_white == False:
                        moves_list.append(self.position[0] + 1, self.position[1] - 1)

                if board_variable[self.position[0][self.position[1] - 1]] != 0:
                    if board_variable[self.position[0]][[self.position[1] - 1]].name == "P" and board_variable[self.position[0] + 1][self.position[1] - 1].is_white == False:
                        if board_variable[self.position[0]][[self.position[1] - 1]].passantable == True:
                            moves_list.append(self.position[0], self.position[1] - 1)
        if self.is_white == False:
            if board_variable[self.position[0] - 1][self.position[1]] == 0:
                moves_list.append(self.position[0] + 1, self.position[1])

                if self.moved == False and board_variable(self.position[0] - 2) == 0:
                    moves_list.append(self.position[0] - 2, self.position[1])
            
            if self.position[1] + 1 <= 7:
                if board_variable[self.position[0] - 1][self.position[1] + 1] != 0:
                    if board_variable[self.position[0] - 1][self.position[1] + 1].is_white == True:
                        moves_list.append(self.position[0] - 1, self.position[1] + 1)

                if board_variable[self.position[0]][[self.position[1] + 1]] != 0:
                    if board_variable[self.position[0]][[self.position[1] + 1]].name == "P" and board_variable[self.position[0]][self.position[1] + 1].is_white == True:
                        if board_variable[self.position[0]][[self.position[1] + 1]].passantable == True:
                            moves_list.append(self.position[0], self.position[1] + 1)

            if self.position[1] - 1 <= 0:
                if board_variable[self.position[0] - 1][self.position[1] - 1] != 0:
                    if board_variable[self.position[0] - 1][self.position[1] - 1].is_white == True:
                        moves_list.append(self.position[0] - 1, self.position[1] - 1)

                if board_variable[self.position[0][self.position[1] - 1]] != 0:
                    if board_variable[self.position[0]][[self.position[1] - 1]].name == "P" and board_variable[self.position[0] + 1][self.position[1] - 1].is_white == True:
                        if board_variable[self.position[0]][[self.position[1] - 1]].passantable == True:
                            moves_list.append(self.position[0], self.position[1] - 1)
        return moves_list

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


