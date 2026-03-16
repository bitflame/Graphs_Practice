from backtracking import is_valid_position


def solve_soduko(board):
    return solve_sudoku_helper(board, 0, 0)


def solve_sudoku_helper(board, start_row, start_col):
    if start_row > 8:
        return True
    row = start_row
    col = start_col
    while board[row][col] != 0:
        col += 1
        if col > 8:
            col = 0
            row += 1
            if row > 8:
                return True
    solved = True
    for num in range(1, 10):
        board[row][col] = num
        if is_valid_position(board):
            if col < 8:
                solved = solve_sudoku_helper(board, row, col + 1)
            else:
                solved = solve_sudoku_helper(board, row + 1, 0)
            if not solved:
                board[row][col] = 0
            else:
                return True
        else:
            # Try the next digit
            board[row][col] = 0
    return False


def is_valid_position(board):
    return check_horizontally(board) and check_vertically(board) and check_boxes(board)


def check_horizontally(board):
    for row in range(9):
        # collect all values of a row in a list
        row_values = [board[row][x] for x in range(9)]
        if not all_desired_numbers(row_values):
            return False
    return True


def check_vertically(board):
    for x in range(9):
        # collect all values of a column in a list
        column_values = [board[row][x] for row in range(9)]
        if not all_desired_numbers(column_values):
            return False
    return True


def check_boxes(board):
    for y_box in range(3):
        for x_box in range(3):
            box_values = collect_box_values(board, y_box, x_box)
            if not all_desired_numbers(box_values):
                return False
    return True


def collect_box_values(board, y_box, x_box):
    box_values = []
    for y in range(3):
        for x in range(3):
            real_y = y_box * 3 + y
            real_x = x_box * 3 + x
            box_values.append(board[real_y][real_x])
    return box_values


def all_desired_numbers(all_collected_values):
    relevant_values = list(all_collected_values)
    # remove the empty field
    relevant_values = remove_all_occurrences(relevant_values, 0)
    values_set = set(relevant_values)
    if len(relevant_values) != len(values_set):
        return False
    return {1, 2, 3, 4, 5, 6, 7, 8, 9}.issuperset(values_set)


def remove_all_occurrences(values, val):
    return [value for value in values if value != val]


def print_array(values):
    for y in range(len(values)):
        for x in range(len(values[y])):
            print(values[y][x], end=" ")
        print()


board = [[1, 2, 0, 4, 5, 0, 7, 8, 9],
         [0, 5, 6, 7, 0, 9, 0, 2, 3],
         [7, 8, 0, 1, 2, 3, 4, 5, 6],
         [2, 1, 4, 0, 6, 0, 8, 0, 7],
         [3, 6, 0, 8, 9, 7, 2, 1, 4],
         [0, 9, 7, 0, 1, 4, 3, 6, 0],
         [5, 3, 1, 6, 0, 2, 9, 0, 8],
         [6, 0, 2, 9, 7, 8, 5, 3, 1],
         [9, 7, 0, 0, 3, 1, 6, 4, 2]]
if solve_soduko(board):
    print("Sudoku is Solved!")
print_array(board)
