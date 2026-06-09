from platform import android_ver


def left_diagnol_clear(grid, current_row, current_col):
    while current_row > -1 and current_col > -1:
        current_row -= 1
        current_col -= 1
        if current_col > -1 and grid[current_row][current_col] == 'Q':
            return False
    return True


def right_diagnol_clear(grid, current_row, current_col):
    while current_row > -1 and current_col < len(grid):
        current_row -= 1
        current_col += 1
        if current_col < len(grid) and grid[current_row][current_col] == 'Q':
            return False
    return True


def vertical_is_clear(grid, current_row, current_col):
    while current_row > -1:
        current_row -= 1
        if grid[current_row][current_col] == 'Q':
            return False
    return True


def start_placing_queens(grid_size, number_of_queens):
    grid = [[' ' for i in range(grid_size)] for j in range(grid_size)]
    return helper_method_to_place_queens(grid, number_of_queens, 0, 0)


def helper_method_to_place_queens(grid, number_of_queens, current_row, current_col):
    solved = False
    if number_of_queens == 0:
        return True
    else:
        for i in range(0, len(grid[0])):
            if (vertical_is_clear(grid, current_row, i) and
                    left_diagnol_clear(grid, current_row, i) and right_diagnol_clear(
                        grid, current_row, i)):
                grid[current_row][i] = 'Q'
                current_col = i
                solved = helper_method_to_place_queens(grid, number_of_queens - 1, current_row + 1,
                                              current_col + 1)
                if not solved : grid[current_row][current_col] = ' '
        return solved


print(start_placing_queens(4, 4))
