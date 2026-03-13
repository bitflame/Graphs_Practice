def edit_distance(str1, str2):
    return helper_str_dist(str1, str2, 0, 0)


def helper_str_dist(str1, str2, current_index, modification_count):
    if len(str1) == 0 and len(str2) == 0:
        return 0
    elif current_index > len(str1)-1 and current_index > len(str2)-1:
        return modification_count
    elif current_index == len(str1)-1 and current_index < len(str2)-1:
        return modification_count + len(str2) - current_index
    elif current_index == len(str2)-1 and current_index < len(str1)-1:
        return modification_count + len(str1) - current_index
    elif len(str1)-1 > current_index and len(str2)-1 > current_index and str1[current_index] != str2[current_index]:
        str1[current_index] = str2[current_index]
        modification_count += 1
        current_index += 1
        return helper_str_dist(str1, str2, current_index, modification_count)
    else:
        current_index += 1
        return helper_str_dist(str1, str2, current_index, modification_count)


str1 = 'A'
str2 = 'A'
print(f'Test 1 - Expected output: 0, actual output: {edit_distance(str1, str2)}')
