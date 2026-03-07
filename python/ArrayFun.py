# The following rearranges an array or a list so even numbers appear before odd numbers. Turns out I did not
# need to check the type. The operation is the same for arrays and lists
import numpy as np


def my_method(numbers):
    if isinstance(numbers, list):
        m = len(numbers)
        write_index = 0
        odds = []
        for i, num in enumerate(numbers):
            if num % 2 == 0:
                numbers[write_index] = num
                write_index += 1
            else:
                odds.append(num)
        for i in range(write_index, m):
            numbers[i] = odds.pop(0)
    if isinstance(numbers, np.ndarray):
        m = numbers.size
    return numbers


first_input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_method(first_input_list)
second_input_list = [2, 4, 6, 1, 8]
my_method(second_input_list)
third_input_list = [2, 4, 6, 8, 1]
my_method(third_input_list)


# the book's way is as follows, which skips over even values and swaps the odds with the next even in the list
# helper functions...
def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def swap(values, first, second):
    tmp = values[first]
    values[first] = values[second]
    values[second] = tmp


def ordder_even_before_odd(numbers):
    i = 0
    while i < len(numbers):
        value = numbers[i]

        if is_even(value):
            i += 1
        else:
            j = i + 1
            while j < len(numbers) and not is_even(numbers[j]):
                j += 1
            if j < len(numbers):
                swap(numbers, i, j)
            else:
                break
            i += 1
