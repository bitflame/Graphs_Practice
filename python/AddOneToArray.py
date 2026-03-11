import numpy as np


def add_one(values):
    if len(values) == 0:
        raise ValueError('There must be at least 1 digit in the number!')
    result = []
    overflow = 1
    for current_digit in reversed(values):
        current_digit += overflow
        overflow = 1 if current_digit >= 10 else 0
        result.insert(0, int(current_digit % 10))
    if overflow == 1:
        result.insert(0, 1)
    return result


my_array = np.array([1, 3, 2, 4])
print(f'expected: [1, 3, 2, 5], actual: {add_one(my_array)} ')
my_array = np.array([1, 4, 8, 9])
print(f'expected: [1, 4, 9, 0], actual: {add_one(my_array)} ')
my_array = np.array([9, 9, 9, 9])
print(f'expected: [0, 0, 0, 0], actual: {add_one(my_array)} ')
