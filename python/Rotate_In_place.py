import numpy as np
from pygments.formatters import load_formatter_from_file


def rotate_in_place(values2dim):
    max_y, max_x = get_dimension(values2dim)
    height = max_y - 1
    width = max_x - 1

    offset = 0
    while offset <= width // 2:
        current_width = width - offset * 2
        for idx in range(current_width):
            # I think lo is LeftOver
            lo_x = offset + idx
            lo_y = offset
            ro_x = width - offset
            ro_y = offset + idx
            ru_x = width - offset - idx
            ru_y = height - offset
            lu_x = offset
            lu_y = height - offset - idx
            lo = values2dim[lo_y][lo_x]
            ro = values2dim[ro_y][ro_x]
            ru = values2dim[ru_y][ru_x]
            lu = values2dim[lu_y][lu_x]
            values2dim[ro_y][ro_x] = lo
            values2dim[ru_y][ru_x] = ro
            values2dim[lu_y][lu_x] = ru
            values2dim[lo_y][lo_x] = lu
        offset += 1


def get_dimension(values2dim):
    if isinstance(values2dim, list):
        return (len(values2dim), len(values2dim[0]))
    if isinstance(values2dim, np.ndarray):
        return values2dim.shape
    raise ValueError("unsupported type", type(values2dim))


my_list = [['1', '2', '3', '4', '5', '6'], ['J', 'K', 'L', 'M', 'N', '7'], ['I', 'V', 'W', 'X', 'O', '8'],
           ['H', 'U', 'Z', 'Y', 'P', '9'],
           ['G', 'T', 'S', 'R', 'Q', '0'], ['F', 'E', 'D', 'C', 'B', 'A']]
rotate_in_place(my_list)


# the copy direction for the following code is opposite to the one before. Unless you look at the
# diagram in the notes, it is not certain you can follow the code. Have a look...
def rotate_inplace_v2(values2dim):
    side_length, _ = get_dimension(values2dim)
    start = 0
    while side_length > 0:
        for i in range(side_length):
            rotate_elements(values2dim, start, side_length, i)

        side_length = side_length - 2
        start += 1


def rotate_elements(values2dim, start, len, i):
    end = start + len - 1
    tmp = values2dim[start][start + 1]
    values2dim[start][start + i] = values2dim[end - i][start]
    values2dim[end - i][start] = values2dim[end][end - i]
    values2dim[end][end - i] = values2dim[start + i][end]
    values2dim[start + i][end] = tmp


def rotate_inplace_recursive(values2dim):
    _, max_x = get_dimension(values2dim)
    __rotate_place_recursive_helper(values2dim, 0, max_x - 1)
    

def __rotate_place_recursive_helper(values2dim, left, right):
    if left >= right:
        return
    current_width = right - left
    for i in range(current_width):
        lo = values2dim[left + i][left]
        ro = values2dim[right][left + i]
        ru = values2dim[right - i][right]
        lu = values2dim[left][right - i]
        values2dim[left + i][left] = ro
        values2dim[right][left + i] = ru
        values2dim[right - i][right] = lu
        values2dim[left][right - i] = lo

    __rotate_place_recursive_helper(values2dim, left + 1, right - 1)
