import numpy as np

from ArrayFun import second_input_list


def my_method(my_data):
    original_length_y = len(my_input_data)  # should be 3
    original_length_x = len(my_input_data[0])  # should be 4
    # print(f'x: {original_length_x} y: {original_length_y}')
    flipped_array = [[0 for _ in range(original_length_y)] for _ in range(original_length_x)]
    for y in range(original_length_y):
        for x in range(original_length_x):
            max_x = original_length_x - 1
            max_y = original_length_y - 1
            orig_value = my_data[y][x]
            # for flipping horizontally...
            new_x = x
            new_y = max_y - y
            flipped_array[new_y][new_x] = orig_value
    return flipped_array


my_input_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_np_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_input_data)
my_method(my_input_data)


# The book uses two pointer left and right to swap symmetric values
def flip_horizontally(value2dim):
    max_y, max_x = get_dimension(value2dim)
    for y in range(max_y):
        left_idx = 0
        right_idx = max_x - 1
        while left_idx < right_idx:
            left_value = value2dim[y][left_idx]
            right_value = value2dim[y][right_idx]
            # swap
            value2dim[y][left_idx] = right_value
            value2dim[y][right_idx] = left_value
            left_idx += 1
            right_idx -= 1
    return value2dim


def swap(values, first, second):
    value1 = vaules[first]
    value2 = vaules[second]
    values[second]=value1
    values[first]=value2

def flip_horizontally_with_swap(values):
    max_x, max_y = get_dimension(vaules)
    for y in range(max_y//2):
        left_idx = 0
        right_idx = max_x-1
        swap(vaules,left_idx,right_idx)

def flip_vertically(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for x in range(max_x):
        top_idx = 0
        bottom_idx = max_y - 1
        while top_idx < bottom_idx:
            top_value = values2dim[top_idx][x]
            bottom_value = values2dim[bottom_idx][x]
            values2dim[top_idx][x] = bottom_value
            values2dim[bottom_idx][x] = top_value
            top_idx += 1
            bottom_idx -= 1


def get_dimension(values2dim):
    if isinstance(values2dim, list):
        return (len(values2dim), len(values2dim[0]))
    if isinstance(values2dim, np.ndarray):
        return values2dim.shape
    raise ValueError("unsupported type", type(values2dim))

print(flip_horizontally(my_input_data))
print('Testing flip_horizontally with Numpy Array.')
print(flip_horizontally(my_np_data))

def is_palindrome(values):
    if isinstance(values, list):
        left, right = 0, len(list) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
    if isinstance(values, np.ndarray):
        left, right = 0, values.size - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
    return True


vaules = np.array(["One", "One"])
print(is_palindrome(vaules))
