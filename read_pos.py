import numpy as np
import pieces as ps

def get_board_array(data_file):
    board = np.genfromtxt(data_file, dtype=str, delimiter=2)
    for n, i in np.ndenumerate(board):
        if 'W' in i:
            is_white = True
        else:
            is_white = False

        if i == '  ':
            board[n] = 0
        elif 'P' in i:
            board[n] = ps.Pawn(n,is_white)
        elif 'R' in i:
            board[n] = ps.Rook(n,is_white)
        elif 'N' in i:
            board[n] = ps.Knight(n,is_white)
        elif 'B' in i:
            board[n] = ps.Bishop(n,is_white)
        elif 'K' in i:
            board[n] = ps.King(n,is_white)
        elif 'Q' in i:
            board[n] = ps.Queen(n,is_white)
    
    return board
        

