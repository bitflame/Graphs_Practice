import numpy as np


def get_dimension(values2dim):
    if isinstance(values2dim, list):
        return len(list), len(list[0])
    if isinstance(values2dim, np.ndarray):
        return values2dim.shape
    raise Exception("unsupported type", type(values2dim))


def place_queen(values2dim, col, row):
    values2dim[row][col] = 'Q'


def remove_queen(values2dim, col, row):
    values2dim[row][col] = ' '


def n_q(board, row):
    max_row, max_col = get_dimension(board)
    if row >= max_row:
        return True
    solved = False
    col = 0
    while col < max_col and not solved:
        if is_valid_position(board, col, row):
            place_queen(board, col, row)
        solved = n_q(board, row + 1)
        if not solved:
            remove_queen(board, col, row)
        col += 1
    return solved


def is_valid_position(values2dim, col, row):
    return 0 < col < len(values2dim[0]) and 0 < row < len(values2dim)


def initialize_board(size):
    return [[' ' for col in range(size)] for row in range(size)]
