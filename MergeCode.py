import itertools


def merge(values1, values2):
    if len(values1) == 0: return values2
    if len(values2) == 0: return values1
    result = []
    v1_idx = 0
    v2_idx = 0
    while v1_idx < len(values1) and v2_idx < len(values2):
        val1 = values1[v1_idx]
        val2 = values2[v2_idx]
        if val1 <= val2:
            result.append(val1)
            v1_idx += 1
        else:
            result.append(val2)
            v2_idx += 1
    result += values1[v1_idx:]
    result += values2[v2_idx:]
    return result


def add_remaining(result, values, pos):
    while pos < len(values):
        result.append(values[pos])
        pos += 1


list_one = [2, 3, 5, 7]
list_two = [11, 13, 17]
print(merge(list_one, list_two))
list_one = [1, 4, 7, 12, 20]
list_two = [10, 15, 17, 33]
print(merge(list_one, list_two))
list_one = [1, 2, 3]
list_two = []
print(merge(list_one, list_two))


def easier_method(values1, values2):
    result = sorted(values1 + values2)


def using_iterators(values1, values2):
    result = []
    iterator1 = iter(values1)
    iterator2 = iter(values2)
    while True:
        try:
            value1, iterator1 = peek(iterator1)
            value2, iterator2 = peek(iterator2)
            if values1 < values2:
                result.append(values1)
                next(iterator1)
            else:
                result.append(values2)
                next(iterator2)
        except StopIteration:
            break
    add_remaining_with_iter(result, iterator1)
    add_remaining_with_iter(result, iterator2)
    return result


def add_remaining_with_iter(result, it):
    while True:
        try:
            value = next(it)
            result.append(value)
        except StopIteration:
            break


def peek(it):
    first = next(it)
    return first, itertools.chain([first], it)

