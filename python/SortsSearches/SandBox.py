def insertion_sort(values):
    for current_pos in range(1, len(values)):
        current_val = values[current_pos]
        insertion_pos = find_insert_pos_from_current(values, current_pos)
        move_right(values, current_pos, insertion_pos)
        values[insertion_pos] = current_val
    return values


def move_right(values, current_pos, insert_pos):
    mov_pos = current_pos
    while insert_pos < mov_pos:
        values[mov_pos] = values[mov_pos - 1]
        mov_pos -= 1


def find_insert_pos_from_current(values, current_pos):
    insert_pos = current_pos
    while values[current_pos] < values[insert_pos - 1] and insert_pos > 0:
        insert_pos -= 1
    return insert_pos


my_test_list = [4, 2, 7, 9, 1]
print(insertion_sort(my_test_list))


def selection_sort(values):
    for i in range(len(values)):
        min_idx = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_idx]:
                min_idx = j
        tmp = values[i]
        values[i] = values[min_idx]
        values[min_idx] = tmp
    return values


my_test_list = [4, 2, 7, 9, 1]
print(my_test_list)
print(insertion_sort(my_test_list))


def merge_sort(to_sort):
    if len(to_sort) <= 1:
        return to_sort
    mid_pos = len(to_sort) // 2
    left = to_sort[0:mid_pos]
    result_left = merge_sort(left)
    right = to_sort[mid_pos:len(to_sort)]
    result_right = merge_sort(right)
    return merge(result_left, result_right)


def merge(left, right):
    result = []
    pos1, pos2 = 0, 0
    while pos1 < len(left) and pos2 < len(right):
        if left[pos1] < right[pos2]:
            result.append(left[pos1])
            pos1 += 1
        else:
            result.append(right[pos2])
            pos2 += 1
    add_remaining(result, left, pos1)
    add_remaining(result, right, pos2)
    return result


def add_remaining(result, values, idx):
    result += values[idx:]


my_test_list = [4, 2, 7, 9, 1]
print(my_test_list)
print("result of merge sort: ", merge_sort(my_test_list))


def merge_sort_with_insertion_sort(to_sort):
    if len(to_sort) < 5:
        insertion_sort(to_sort)
        return to_sort
    mid_pos = len(to_sort) // 2
    left = to_sort[0:mid_pos]
    result_left = merge_sort(left)
    right = to_sort[mid_pos:len(to_sort)]
    result_right = merge_sort(right)
    return merge(result_left, result_right)


my_test_list = [4, 2, 7, 9, 1, 3, 11, 5, 6, 14]
print(my_test_list)
print("result of merge sort with insertion sort: ", merge_sort_with_insertion_sort(my_test_list))


def quick_sort(values):
    if len(values) <= 1:
        return values
    pivot = values[0]
    below_or_equal = [val for val in values[1:] if val <= pivot]
    aboves = [val for val in values[1:] if val > pivot]
    sorted_lower_parts = quick_sort(below_or_equal)
    sorted_uppers_part = quick_sort(aboves)
    return sorted_lower_parts + [pivot] + sorted_uppers_part


my_test_list = [4, 2, 7, 9, 1, 3, 11, 5, 6, 14]
print(my_test_list)
print("result of merge sort with insertion sort: ", quick_sort(my_test_list))


def binary_search(values, target, low, hi=None):
    if hi is None:
        hi = len(values) - 1
    if low > hi:
        return -1
    mid = (hi + low) // 2
    if values[mid] == target:
        return mid
    elif values[mid] > target:
        return binary_search(values, target, low, mid - 1)
    elif values[mid] < target:
        return binary_search(values, target, mid + 1, hi)
    return None


search_values = [7, 2]


# this needs the array to be sorted
def contains_all(values, search_values):
    for val in search_values:
        if binary_search(values, val, 0) == -1:
            return False
    return True


# this works in arrays not sorted
def better_contains(values, search_values):
    for val in search_values:
        if val not in values:
            return False
    return True


def contains_all_via_set(values, search_values):
    set_values = set(values)
    for search_val in search_values:
        if search_val not in set_values:
            return False
    return True


values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('looking for 15 in array of 0 to 10 expected value: -1, actual value: ', binary_search(values, 15, 0))
print('looking for -1 in array of 0 to 10 expected value: -1, actual value: ', binary_search(values, -1, 0))
print('looking for 0 in array of 0 to 10 expected value: 0, actual value: ', binary_search(values, 0, 0))
print('looking for 1 in array of 0 to 10 expected value: 1, actual value: ', binary_search(values, 1, 0))
print('looking for 2 in array of 0 to 10 expected value: 2, actual value: ', binary_search(values, 2, 0))
print('looking for 3 in array of 0 to 10 expected value: 3, actual value: ', binary_search(values, 3, 0))
print('looking for 4 in array of 0 to 10 expected value: 4, actual value: ', binary_search(values, 4, 0))
print('looking for 5 in array of 0 to 10 expected value: 5, actual value: ', binary_search(values, 5, 0))
print('looking for 6 in array of 0 to 10 expected value: 6, actual value: ', binary_search(values, 6, 0))
print('looking for 7 in array of 0 to 10 expected value: 7, actual value: ', binary_search(values, 7, 0))
print('looking for 8 in array of 0 to 10 expected value: 8, actual value: ', binary_search(values, 8, 0))
print('looking for 9 in array of 0 to 10 expected value: 9, actual value: ', binary_search(values, 9, 0))

print('values: ', values)
print('using sorted on the values list', sorted(values))
print('values: ', values)

#################################Testing contains_all()#####################################
print('--------------------------Testing contains_all()-----------------------------------')
print('expected outcome: True, actual outcome: ', contains_all(values, search_values))
false_search_values = [5, 11]
print('expected outcome: False, actual outcome: ', contains_all(values, false_search_values))
false_search_values = [0, 9, 5, 11, 0]
print('expected outcome: False, actual outcome: ', contains_all(values, false_search_values))
#################################Testing better_contains()#####################################
print('--------------------------Testing better_contains()-----------------------------------')
print('expected outcome: True, actual outcome: ', better_contains(values, search_values))
false_search_values = [5, 11]
print('expected outcome: False, actual outcome: ', better_contains(values, false_search_values))
false_search_values = [0, 9, 5, 11, 0]
print('expected outcome: False, actual outcome: ', better_contains(values, false_search_values))
#################################Testing contains_all_via_set()#####################################
print('--------------------------Testing contains_all_via_set()-----------------------------------')
print('expected outcome: True, actual outcome: ', contains_all_via_set(values, search_values))
false_search_values = [5, 11]
print('expected outcome: False, actual outcome: ', contains_all_via_set(values, false_search_values))
false_search_values = [0, 9, 5, 11, 0]
print('expected outcome: False, actual outcome: ', contains_all_via_set(values, false_search_values))


def yet_another_contains_all(values, search_values):
    values_set = set(values)
    return all(val in values_set for val in search_values)
    # return all(val in search_values for val in values_set)


#################################Testing yet_another_contains_all()#####################################
print('--------------------------Testing yet_another_contains_all()-----------------------------------')
print('expected outcome: True, actual outcome: ', yet_another_contains_all(values, search_values))
false_search_values = [5, 11]
print('expected outcome: False, actual outcome: ', yet_another_contains_all(values, false_search_values))
false_search_values = [0, 9, 5, 11, 0]
print('expected outcome: False, actual outcome: ', yet_another_contains_all(values, false_search_values))
#################################Testing partition2()#####################################
print('--------------------------Testing partition2()-----------------------------------')


def partition2(text):
    result = str.join("", partition2_helper(text[0], 1, len(text) - 1, list(text)))
    return result


def partition2_helper(pivot, head_idx, end_idx, text):
    if head_idx >= end_idx:
        return text
    if text[head_idx] == pivot:
        head_idx += 1
    elif text[head_idx] != text[end_idx]:
        tmp = text[head_idx]
        text[head_idx] = text[end_idx]
        text[end_idx] = tmp
    if text[end_idx] != pivot:
        end_idx -= 1
    elif text[head_idx] != text[end_idx]:
        tmp = text[head_idx]
        text[head_idx] = text[end_idx]
        text[end_idx] = tmp
        head_idx += 1
        end_idx -= 1
    return partition2_helper(pivot, head_idx, end_idx, text)


text = "ABAABBBAAABBBA"
print(partition2(text))


def book_method(text):
    low = 0
    high = len(text) - 1
    while low <= high:
        if text[low] == 'A':
            low += 1
        else:
            swap_positions(text, low, high)
            high -= 1
    return "".join(text)


def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


text = "ABAABBBAAABBBA"
# print(book_method(text))
############################Testing partition_three_chars()###############################
print('---------------------Testing partition_three_chars()-----------------------------')


# assuming the pivot value is know...
def part_three(text):
    text_list = list(text)
    low = 0
    mid = 0
    high = len(text) - 1
    while mid <= high:
        if text_list[mid] == 'A':
            swap_positions(text_list, low, mid)
            mid += 1
            low += 1
        elif text_list[mid] == 'B':
            mid += 1
        else:
            swap_positions(text_list, mid, high)
            high -= 1
    return str.join("", text_list)


print(part_three("ABACCBBCAACCBBA"))


def my_method(values):
    start, mid, end = 0, 0, len(values) - 1
    values_list = list(values)
    while mid < end:
        if values_list[mid] == 'A':
            swap_positions(values_list, start, mid)
            start += 1
            mid += 1
        elif values_list[mid] == 'B':
            mid += 1

        else:  # values[mid] must be a 'C'
            swap_positions(values_list, mid, end)
            end -= 1
    return str.join("", values_list)


values = 'ABCABCABCABC'
print('Test 1 - input: ABCABCABCABC, expected output: AAAABBBBCCCC, actual output: ', my_method(values))
values = 'AAB'
print('Test 2 - input: AAB, expected output: AAB, actual output: ', my_method(values))
values = 'ABA'
print('Test 3 - input: ABA, expected output: AAB, actual output: ', my_method(values))
values = 'ACB'
print('Test 4 - input: ACB, expected output: ABC, actual output: ', my_method(values))
