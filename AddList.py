def safe_get_at(values, pos):
    if 0 <= pos <= len(values):
        return values[pos]
    return 0


def safer_get_at(values, pos):
    try:
        return values[pos]
    except IndexError:
        return 0


def yet_another(val_list_1, val_list_2):
    result = []
    sum, first_val, second_val, carry = 0, 0, 0, 0
    v1, v2 = len(val_list_1) - 1, len(val_list_2) - 1
    while v1 >= 0 or v2 >= 0:
        first_val = safe_get_at(val_list_1, v1)
        second_val = safe_get_at(val_list_2, v2)
        sum = first_val + second_val + carry
        result.insert(0, sum % 10)
        if sum > 9:
            carry = 1
        else:
            carry = 0
        v1 -= 1
        v2 -= 1
    if carry == 1:
        result.insert(0, 1)
    return result


va_list_1 = [1, 2, 3]
va_list_2 = [9, 2, 7]
print(yet_another(va_list_1, va_list_2))
va_list_1 = [4, 5, 6]
va_list_2 = [1, 3, 5]
print(yet_another(va_list_1, va_list_2))
va_list_1 = [5, 7, 9]
va_list_2 = [1, 0, 6, 2]
print(yet_another(va_list_1, va_list_2))


def process_revrse(l1, l2):
    v1, v2, value1, value2, carry = 0, 0, 0, 0, 0
    sum_res = 0
    result = []
    while v1 < len(l1) or v2 < len(l2):
        value1 = safe_get_at(l1, v1)
        value2 = safe_get_at(l2, v2)
        sum_res = value1 + value2 + carry
        carry = 1 if sum_res > 9 else 0
        # result.insert(0, sum_res % 10)
        result.append(sum_res%10)
        v1 += 1
        v2 += 1
    if carry == 1: result.append(carry)
    return result


lis1 = [3, 2, 1]
lis2 = [7, 2, 9]
process_revrse(lis1, lis2)
