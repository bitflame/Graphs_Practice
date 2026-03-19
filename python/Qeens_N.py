def left_diagnol_clear(grid, current_row, current_col):
    while current_row > -1 and current_col > -1:
        current_row -= 1
        current_col -= 1
        if grid[current_row][current_col] == 'Q':
            return False
    return True


def right_diagnol_clear(grid, current_row, current_col):
    while current_row > -1 and current_col < len(grid):
        if grid[current_row][current_col] == 'Q':
            return False
        current_row -= 1
        current_col += 1
    return True


def vertical_is_clear(grid, current_row, current_col):
    while current_row > -1:
        if grid[current_row][current_col] == 'Q':
            return False
        current_row -= 1
    return True


def start_placing_queens(grid_size, number_of_queens):
    grid = [[' ' for i in range(grid_size)] for j in range(grid_size)]
    return helper_method_to_place_queens(grid, number_of_queens, 0, 0)


def helper_method_to_place_queens(grid, number_of_queens, current_row, current_col):
    if number_of_queens == 0:
        return grid
    else:
        grid[current_row][current_col] = 'Q'
        if (vertical_is_clear(grid, current_row, current_col)
                and left_diagnol_clear(grid, current_row,current_col)
                and right_diagnol_clear(grid, current_row, current_col)):
            helper_method_to_place_queens(grid, number_of_queens - 1, current_row + 1, current_col)
        else:
            helper_method_to_place_queens(grid, number_of_queens, current_row, current_col + 1)


start_placing_queens(4, 4)
