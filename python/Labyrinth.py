def find_way_out(values, x, y):
    if 0 > x or y < 0 or x > len(values[0]) or y > len(values):
        return False

    if values[y][x] == 'X':
        print(f'Found an exit at row: {y} and col: {x}')
        return True
    if values[y][x] in '.#':
        return False
    if values[y][x] == ' ':
        values[y][x] = '.'
    up = find_way_out(values, x, y - 1)
    down = find_way_out(values, x, y + 1)
    left = find_way_out(values, x - 1, y)
    right = find_way_out(values, x + 1, y)
    found_a_way = up or down or left or right
    if not found_a_way:
        values[y][x] = ' '
    return found_a_way


labyrinth = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', ' ', 'X'],
    ['#', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '.', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', 'X', '#', '#', '#']
]

find_way_out(labyrinth, 1, 1)


def print_lab(labyrinth):
    for y in range(len(labyrinth)):
        for x in range(len(labyrinth[0])):
            print(labyrinth[y][x], end='')
        print()


print_lab(labyrinth)

labyrinth = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', ' ', 'X'],
    ['#', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '.', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', 'X', '#', '#', '#']
]


def find_way_out_v2(board, x, y):
    if x < 0 or x > len(board[0])-1 or y < 0 or y > len(board)-1: return False
    if board[y][x] == '#':
        return False
    found = board[y][x] == 'X'
    if found:
        print("FOUND EXIT: X: {}, Y: {}".format(x, y))
    board[y][x] = '#'
    right = find_way_out_v2(board, x + 1, y)
    left = find_way_out_v2(board, x - 1, y)
    down = find_way_out_v2(board, x, y + 1)
    up = find_way_out_v2(board, x, y - 1)
    return found or right or left or down or up


find_way_out_v2(labyrinth, 1, 1)
# printing labyrinth after running version 2
print_lab(labyrinth)
