def check_horizontally(board):
    # collect all the values in a row
    for row in range(9):
        row_values = [board[row][x] for x in range(9)]
        if not all_desired_numbers(row_values):
            return False
    return True


def check_vertically(board):
    for x in range(9):
        col_values = [board[row][x] for row in range(9)]
        if not all_desired_numbers(col_values):
            return False
    return True


def all_desired_numbers(all_collected_values):
    if len(all_collected_values) != 9:
        raise ValueError('Each row should have exactly nine values.')
    one_to_nine = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    values_set = set(all_collected_values)
    return values_set == one_to_nine

def check_boxes(board):
    for y_box in range(3):
        for x_box in range(3):
            box_values =  collect_box_values(board, y_box, x_box)

            if not all_desired_numbers(box_values):
                return False
    return True
def collect_box_values(board, y_box, x_box):
    box_values = []
    for y in range(3):
        for x in range(3):
            real_y = y_box*3+y
            real_x = x_box*3+x
            box_values.append(board[real_y][real_x])
    return box_values

def is_sudoku_valid(board):
    return check_horizontally(board) and check_vertically(board) and check_boxes(board)

