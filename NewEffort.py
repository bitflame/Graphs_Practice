import random
from datetime import datetime


def puzzle_solver(board):
    return puzzle_solver_helper(board, 0, 0)


# will return true if the puzzle is solvable and solved
def puzzle_solver_helper(board, start_row, start_col):
    if start_row > 8:
        return True
    row = start_row
    col = start_col
    while board[row][col] != "0":
        col += 1
        if col > 8:
            row += 1
            col = 0
            if row > 8:
                return True
    solved = True
    for num in range(1, 10):
        board[row][col] = num
        if is_valid_position(board):


def is_valid_position(board):
    return check_horizontally(board) and check_vertically(board) and check_box(board)


def remove_all_occurrences(values, val):
    return [value for value in values if value != val]


def check_vertically(board):
    for x in range(9):
        col_values =[board[row][x] for row in range(9)]
        if not all_desired_numbers(col_values):
            return False
    return True

# checks every row for having desired values i.e. it checks every col for every row every time it is called
def check_horizontally(values):
    for row in values:
        row_values = [values[row][x] for x in range(9)]
        if not all_desired_numbers(row_values):
            return False
    return True


# checks all the numbers in a list for redundancy and they are within 0 and 9
def all_desired_numbers(all_collected_values):
    relevant_values = list(all_collected_values)
    relevant_values = remove_all_occurrences(relevant_values, 0)
    value_set = set(relevant_values)
    if len(value_set) != len(relevant_values): return False
    return value_set.issubset([1, 2, 3, 4, 5, 6, 7, 8, 9])


# 0 represents a blank spot
def create_sudoku_board():
    board = [[random.randint(0, 9) for i in range(9)] for j in range(9)]
    return board


my_board = create_sudoku_board()
stamp = datetime.today()
print(stamp.strftime('%B %d, %Y'))


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], ' ', end='')
        print()
    return None


print_board(my_board)
