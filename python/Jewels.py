import random
from sys import orig_argv

import numpy as np


def init_jewels_board(width, height, num_of_colors):
    board = [[0 for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            board[y][x] = select_valid_jewel(board, x, y, num_of_colors)
    return board


def select_valid_jewel(board, x, y, num_of_colors):
    next_jewel_nr = -1
    is_valid = False
    while not is_valid:
        next_jewel_nr = random.randint(1, num_of_colors)
        is_valid = not check_horizontally(board, x, y, next_jewel_nr) and not check_vertically(board, x, y,
                                                                                               next_jewel_nr) and not check_diagonally(
            board, x, y, next_jewel_nr)
    return next_jewel_nr


def check_horizontally(board, x, y, jewel_nr):
    top1 = get_at(board, x, y - 1)
    top2 = get_at(board, x, y - 2)
    return top1 == jewel_nr and top2 == jewel_nr


def check_vertically(board, x, y, jewel_nr):
    left1 = get_at(board, x - 1, y)
    left2 = get_at(board, x - 2, y)
    return left1 == jewel_nr and left2 == jewel_nr


def get_at(values, x, y):
    max_y, max_x = get_dimension(values)
    if x < 0 or y < 0 or y >= max_y or x >= max_x:
        return -1

    return values[y][x]


def get_dimension(values2dim):
    if isinstance(values2dim, list):
        return (len(values2dim), len(values2dim[0]))
    if isinstance(values2dim, np.ndarray):
        return values2dim.shape
    raise ValueError('Unsupported type', type(values2dim))


def check_diagonally(board, x, y, jewel_nr):
    up_left1 = get_at(board, x - 1, y)
    up_left2 = get_at(board, x - 2, y)
    up_right1 = get_at(board, x + 1, y)
    up_right2 = get_at(board, x + 2, y)
    return (up_left1 == jewel_nr and up_left2 == jewel_nr) or (up_right1 == jewel_nr and up_right2 == jewel_nr)


def erase_chains(values2dim):
    mark_elements_for_removal(values2dim)

    return erase_all_marked(values2dim)


def mark_elements_for_removal(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for y in range(max_y):
        for x in range(max_x):
            dirs_with_chains = find_chains(values2dim, x, y)

            mark_chains_for_removal(values2dim, x, y)


def erase_all_marked(values2dim):
    erased_something = False
    max_y, max_x = get_dimension(values2dim)
    for y in range(max_y):
        for x in range(max_x):
            if is_element_marked_for_removal(values2dim[y][x]):
                values2dim[y][x] = blank_value(values2dim)
                erased_something = True

    return erased_something


def is_element_marked_for_removal(value):
    return value < 0


def blank_value(values2dim):
    return 0


def find_chains(values2dim, start_x, start_y):
    orig_value = values2dim[start_y][start_x]
    if orig_value == 0:
        return []
    dirs_with_chains = []

    relevant_dirs = (Direction.S, Direction.SW, Direction.E, Direction.SE)

    for current_dir in relevant_dirs:
        length = 1

    dx, dy = current_dir.value
    next_pos_x = start_x + dx
    next_pos_y = start_y + dy
    while is_on_board(values2dim, next_pos_x, next_pos_y) and is_same(orig_value, values2dim[next_pos_y][next_pos_x]):
        length += 1
        next_pos_x += dx
        next_pos_y += dy
        if length >= 3:
            dirs_with_chains.append(current_dir)
    return dirs_with_chains


def is_on_board(values2dim, next_pos_x, next_pos_y):
    max_y, max_x = get_dimension(values2dim)
    return 0 <= next_pos_x < max_x and 0 <= next_pos_y < max_y


def is_same(val1, val2):
    return abs(val1) == abs(val2)


def mark_chains_for_removal(values, start_x, start_y, dirs_with_chains):
    orig_value = values[start_y][start_x]
    for current_dir in dirs_with_chains:
        dx, dy = current_dir.value
        next_x = start_x
        next_y = start_y
        while is_on_board(values, next_x, next_y) and is_same(orig_value, values[next_y][next_x]):
            values[next_y][next_x] = mark_chains_for_removal(orig_value)
            next_x += dx
            next_y += dy


def mark_element_for_removal(value):
    return -value if value > 0 else value
