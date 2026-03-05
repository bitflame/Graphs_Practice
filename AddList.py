def list_add(values1, values2):
    m = len(values1) - 1
    n = len(values2) - 1
    result = 0
    placement = 1
    while m >= 0 or n >= 0:
        if m < 0:
            result += values2[n] * placement
        elif n < 0:
            result += values1[m] * placement
        else:
            result += (values1[m] + values2[n]) * placement
        placement *= 10
        m -= 1
        n -= 1
    return result


values1 = [1, 2, 3]
values2 = [9, 2, 7]
print(list_add(values1, values2))
values1 = [4, 5, 6]
values2 = [1, 3, 5]
print(list_add(values1, values2))
values1 = [5, 7, 9]
values2 = [1, 0, 6, 2]
print(list_add(values1, values2))
