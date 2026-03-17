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
    while board[row][col] != 0:
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
            if col < 8:
                solved = puzzle_solver_helper(board, row, col + 1)
            else:
                solved = puzzle_solver_helper(board, row + 1, 0)
            if not solved:
                board[row][col] = 0
            else:
                return True
        else:
            board[row][col] = 0
    return False


def is_valid_position(board):
    return check_horizontally(board) and check_vertically(board) and check_boxes(board)


def check_boxes(board):
    for y_box in range(3):
        for x_box in range(3):
            box_values = collect_box_values(board, y_box, x_box)
            if not all_desired_numbers(box_values):
                return False
    return True


def collect_box_values(board, y, x):
    box_values = []
    for row in range(3):
        for col in range(3):
            box_values.append(board[y * 3 + row][x * 3 + col])
    return box_values


def remove_all_occurrences(values, val):
    return [value for value in values if value != val]


# checks the board one column at a time for valid content
def check_vertically(board):
    for x in range(9):
        col_values = [board[row][x] for row in range(9)]
        if not all_desired_numbers(col_values):
            return False
    return True


# checks every row for having desired values i.e. it checks every col for every row every time it is called
def check_horizontally(values):
    for row in range(9):
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


some_board = [[1, 2, 0, 4, 5, 0, 7, 8, 9],
              [0, 5, 6, 7, 0, 9, 0, 2, 3],
              [7, 8, 0, 1, 2, 3, 4, 5, 6],
              [2, 1, 4, 0, 6, 0, 8, 0, 7],
              [3, 6, 0, 8, 9, 7, 2, 1, 4],
              [0, 9, 7, 0, 1, 4, 3, 6, 0],
              [5, 3, 1, 6, 0, 2, 9, 0, 8],
              [6, 0, 2, 9, 7, 8, 5, 3, 1],
              [9, 7, 0, 0, 3, 1, 6, 4, 2]]
print("-----Here is the result of current code:")
print(puzzle_solver(some_board))


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
print("Here is the board after solving it: ")
print_board(some_board)
print_board(my_board)


def get_row(board):
    print('Here are the rows one at a time ')
    for row in range(9):
        current_row = [board[row][col] for col in range(9)]


get_row(my_board)


def get_column(board):
    for col in range(9):
        current_column = [board[row][col] for row in range(9)]
