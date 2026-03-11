def array_split_inplace(values, reference_element):
    low = 0
    high = len(values) - 1
    while low < high:
        while low < high and values[low] < reference_element:
            low += 1
        while high > low and values[high] >= reference_element:
            high -= 1
        if low < high:
            swap(values, low, high)
    if len(values[high + 1:]) == 0:
        return values[:high + 1] + [reference_element]
    else:
        return values[:high] + [reference_element] + values[high:]


def swap(values, low, hi):
    val1 = values[low]
    val2 = values[hi]
    values[hi] = val1
    values[low] = val2


my_values = [9, 4, 7, 1, 20]
print(array_split_inplace(my_values, 9))
my_values = [7, 3, 5, 2]
print(array_split_inplace(my_values, 7))
my_values = [7, 2, 14, 10, 1, 11, 12, 3, 4]
print(array_split_inplace(my_values, 7))
my_values = [11, 3, 5, 7, 1, 11, 13, 17, 19]
print(array_split_inplace(my_values, 11))
