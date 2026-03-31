from tokenize import endpats

from numpy.ma.core import maximum_fill_value

from org.example.strings import mid_chars


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
    while mid <= end:
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
values = 'CBA'
print('Test 5 - input: CBA, expected output: ABC, actual output: ', my_method(values))
values = 'CCBA'
print('Test 6 - input: CCBA, expected output: ABCC, actual output: ', my_method(values))
values = "ABACCBBCAACCBBA"
print('Test 7 - input: ABACCBBCAACCBBA, expected output: AAAAABBBBBCCCCC, actual output: ', my_method(values))

print('---------------------BinarySearch Recursive -----------------------------')


def another_binary_search(values, target):
    return another_binary_search_helper(values, target, 0, len(values) - 1)


def another_binary_search_helper(values, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if values[mid] == target:
        return values[mid]
    elif values[mid] > target:
        return another_binary_search_helper(values, target, lo, mid - 1)
    elif values[mid] < target:
        return another_binary_search_helper(values, target, mid + 1, hi)
    return None


values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print('Test 1 - input: values:1,2,3,4,5,6,7,8,9, target: 5, output:  ', another_binary_search(values, 5))
target = 14
print('Test 2 - input: values:1,2,3,4,5,6,7,8,9, target: 14, output:  ', another_binary_search(values, 14))
target = 0
print('Test 3 - input: values:1,2,3,4,5,6,7,8,9, target: 0, output:  ', another_binary_search(values, 0))
print('Test 4 - input: values:1,2,3,4,5,6,7,8,9, target: 1, output:  ', another_binary_search(values, 1))
print('Test 5 - input: values:1,2,3,4,5,6,7,8,9, target: 2, output:  ', another_binary_search(values, 2))
print('Test 6 - input: values:1,2,3,4,5,6,7,8,9, target: 3, output:  ', another_binary_search(values, 3))
print('Test 7 - input: values:1,2,3,4,5,6,7,8,9, target: 4, output:  ', another_binary_search(values, 4))
print('Test 8 - input: values:1,2,3,4,5,6,7,8,9, target: 5, output:  ', another_binary_search(values, 5))
print('Test 9 - input: values:1,2,3,4,5,6,7,8,9, target: 6, output:  ', another_binary_search(values, 6))
print('Test 10 - input: values:1,2,3,4,5,6,7,8,9, target: 7, output:  ', another_binary_search(values, 7))
print('Test 11 - input: values:1,2,3,4,5,6,7,8,9, target: 8, output:  ', another_binary_search(values, 8))
print('Test 12 - input: values:1,2,3,4,5,6,7,8,9, target: 9, output:  ', another_binary_search(values, 9))
print('Test 13 - input: values:1,2,3,4,5,6,7,8,9, target: 10, output:  ', another_binary_search(values, 10))

print('---------------------BinarySearch Recursive Returns True/False-----------------------------')


# Michael Inden does it this way...
def bin_search(sorted_values, search_for):
    mid_pos = len(sorted_values) // 2
    if search_for == sorted_values[mid_pos]:
        return True
    if len(sorted_values) > 1:
        if sorted_values[mid_pos] > search_for:
            lower_helf = sorted_values[0:mid_pos]
            return bin_search(lower_helf, search_for)
        elif sorted_values[mid_pos] < search_for:
            upper_half = sorted_values[mid_pos + 1:len(sorted_values)]
            return bin_search(upper_half, search_for)
    return False


print('Test 1 - input: values:1,2,3,4,5,6,7,8,9, target: 5, output:  ', bin_search(values, 5))
print('Test 2 - input: values:1,2,3,4,5,6,7,8,9, target: 0, output:  ', bin_search(values, 0))
print('Test 3 - input: values:1,2,3,4,5,6,7,8,9, target: 14, output:  ', bin_search(values, 14))

############################BinarySearch Iterative###############################
print('---------------------BinarySearch Iterative-----------------------------')


def bin_search_iter(values, target):
    lo, mid, hi = 0, 0, len(values) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if values[mid] == target:
            return values[mid]
        elif values[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


print('Test 1 - input: values:1,2,3,4,5,6,7,8,9, target: 5, output:  ', bin_search_iter(values, 5))
print('Test 2 - input: values:1,2,3,4,5,6,7,8,9, target: 15, output:  ', bin_search_iter(values, 15))
print('Test 3 - input: values:1,2,3,4,5,6,7,8,9, target: 0, output:  ', bin_search_iter(values, 0))
print('Test 4 - input: values:1,2,3,4,5,6,7,8,9, target: 1, output:  ', bin_search_iter(values, 1))
print('Test 5 - input: values:1,2,3,4,5,6,7,8,9, target: 2, output:  ', bin_search_iter(values, 2))
print('Test 6 - input: values:1,2,3,4,5,6,7,8,9, target: 3, output:  ', bin_search_iter(values, 3))
print('Test 7 - input: values:1,2,3,4,5,6,7,8,9, target: 4, output:  ', bin_search_iter(values, 4))
print('Test 8 - input: values:1,2,3,4,5,6,7,8,9, target: 5, output:  ', bin_search_iter(values, 5))
print('Test 9 - input: values:1,2,3,4,5,6,7,8,9, target: 6, output:  ', bin_search_iter(values, 6))
print('Test 10 - input: values:1,2,3,4,5,6,7,8,9, target: 7, output:  ', bin_search_iter(values, 7))
print('Test 11 - input: values:1,2,3,4,5,6,7,8,9, target: 8, output:  ', bin_search_iter(values, 8))
print('Test 12 - input: values:1,2,3,4,5,6,7,8,9, target: 9, output:  ', bin_search_iter(values, 9))
print('Test 13 - input: values:1,2,3,4,5,6,7,8,9, target: 10, output:  ', bin_search_iter(values, 10))
################################Insertion Sort##########################################
print('--------------------------Insertion Sort---------------------------------------')


def insertion_sort(values):
    curr = 0
    while curr < len(values):
        if curr > 0 and values[curr - 1] > values[curr]:
            tmp = values[curr]
            tmp_cntr = curr
            while tmp_cntr > 0 and values[tmp_cntr - 1] > tmp:
                values[tmp_cntr] = values[tmp_cntr - 1]
                tmp_cntr -= 1
            values[tmp_cntr] = tmp
        curr += 1
    return values


values = [7, 2]
print('Test 1 - Expecting 2,7: ', insertion_sort(values))
values = [2, 7]
print('Test 2 - Expecting 2,7: ', insertion_sort(values))
values = [7, 2, 5, 1, 6, 8, 9, 4, 2]
print('Test 3 - Expecting 1,2,4,5,6,7,8,9: ', insertion_sort(values))
values = [2, 7, 5, 1, 6, 8, 9, 4, 2]
print('Test 4 - Expecting 1,2,4,5,6,7,8,9: ', insertion_sort(values))
values = [7, 2, 5, 1, 6, 8, 9, 4, 3]
print('Test 5 - Expecting 1,2,4,5,6,7,8,9: ', insertion_sort(values))


def ins_sort_book(values):
    for i in range(1, len(values)):
        # check if the current element is smaller than predecessor
        current_idx = i
        while values[current_idx] > 0 and values[current_idx] < values[current_idx - 1]:
            swap_positions(values, current_idx - 1, current_idx)
            current_idx -= 1


################################Selection Sort##########################################
def my_selection(values):
    end = len(values) - 1
    while end > 0:
        max_val_idx = 0
        curr = 1
        while curr <= end:
            if values[curr] > values[max_val_idx]:
                max_val_idx = curr
            curr += 1
        values[max_val_idx], values[end] = values[end], values[max_val_idx]
        end -= 1
    return values


values = [7, 2]
print('Test 1 - Expecting 2,7: ', my_selection(values))
values = [2, 7]
print('Test 2 - Expecting 2,7: ', my_selection(values))
values = [7, 2, 5, 1, 6, 8, 9, 4, 2]
print('Test 3 - Expecting 1,2,4,5,6,7,8,9: ', my_selection(values))
values = [2, 7, 5, 1, 6, 8, 9, 4, 2]
print('Test 4 - Expecting 1,2,4,5,6,7,8,9: ', my_selection(values))
values = [7, 2, 5, 1, 6, 8, 9, 4, 3]
print('Test 5 - Expecting 1,2,4,5,6,7,8,9: ', my_selection(values))


def book_selection_sort(value):
    for i in range(len(values) - 1, 0, -1):
        max_pos = find_max_pos(values, 0, i + 1)
        swap_positions(values, max_pos, i)
    return values


def find_max_pos(values, start_pos, end_pos):
    max_pos = start_pos
    for i in range(start_pos + 1, end_pos):
        if values[i] > values[max_pos]:
            max_pos = i

    return max_pos


values = [7, 2]
print('Test 1 - Expecting 2,7: ', book_selection_sort(values))
values = [2, 7]
print('Test 2 - Expecting 2,7: ', book_selection_sort(values))
values = [7, 2, 5, 1, 6, 8, 9, 4, 2]
print('Test 3 - Expecting 1,2,4,5,6,7,8,9: ', book_selection_sort(values))
values = [2, 7, 5, 1, 6, 8, 9, 4, 2]
print('Test 4 - Expecting 1,2,4,5,6,7,8,9: ', book_selection_sort(values))
values = [7, 2, 5, 1, 6, 8, 9, 4, 3]
print('Test 5 - Expecting 1,2,4,5,6,7,8,9: ', book_selection_sort(values))

################################Quick Sort##########################################
print("-------------------------Quick Sort----------------------------------------")


def my_quick_sort(values):
    return my_quick_sort_helper(values, 0, len(values) - 1)


def my_quick_sort_helper(values, left, right):
    if left >= right:
        return
    partition_index = partition(values, left, right)
    my_quick_sort_helper(values, left, partition_index - 1)
    my_quick_sort_helper(values, partition_index + 1, right)


def partition(values, left, right):
    pivot = values[0]
    left_idx = left + 1
    right_idx = right
    while left_idx < right_idx:
        while left_idx < right_idx and values[left_idx] < pivot:
            left_idx += 1
        while right_idx > left_idx and values[right_idx] > pivot:
            right_idx -= 1
        if left_idx < right_idx:
            swap_positions(values, left_idx, right_idx)
    if values[right_idx] < pivot:
        swap_positions(values, left, right_idx)
    return right_idx


values = [7, 2]
my_quick_sort(values)
print('Test 1 - Expecting 2,7: ', values)
values = [2, 7]
my_quick_sort(values)
print('Test 2 - Expecting 2,7: ', values)
values = [7, 2, 5, 1, 6, 8, 9, 4, 2]
my_quick_sort(values)
print('Test 3 - Expecting 1,2,4,5,6,7,8,9: ', values)
values = [2, 7, 5, 1, 6, 8, 9, 4, 2]
my_quick_sort(values)
print('Test 4 - Expecting 1,2,4,5,6,7,8,9: ', values)
values = [7, 2, 5, 1, 6, 8, 9, 4, 3]
my_quick_sort(values)
print('Test 5 - Expecting 1,2,4,5,6,7,8,9: ', values)

################################Bucket Sort##########################################
print("-------------------------Bucket Sort----------------------------------------")


def my_bucket_sort(values):
    data_dictionary = {}
    result = []
    for val in values:
        if val not in data_dictionary.keys():
            data_dictionary[val] = 1
        else:
            data_dictionary[val] = data_dictionary[val] + 1
    for key in sorted(data_dictionary.keys()):
        for i in range(data_dictionary[key]):
            result.append(key)
    return result


ages = [10, 50, 22, 7, 42, 111, 50, 7]
print(my_bucket_sort(ages))


# AI generated version
def my_bucket_sort(values):
    freq = {}

    for v in values:
        freq[v] = freq.get(v, 0) + 1

    result = []
    for key in sorted(freq):
        result.extend([key] * freq[key])

    return result


def bucket_sort(values, max_value):
    buckets = [0] * max_value
    fill_bucket(values, buckets)
    results = [0] * len(values)
    return fill_result_from_buckets(buckets, results)


def fill_bucket(values, buckets):
    for val in values:
        buckets[val] += 1
    return buckets


def fill_result_from_buckets(bucket, results):
    index = 0
    for i, val in enumerate(bucket):
        for j in range(val):
            results[index] = i
            index += 1
    return results


print(bucket_sort(ages, 150))


#########################################Rotated BinarySearch###################################################
def find_flank_pos(values):
    return find_flank_pos_in_range(values, 0, len(values) - 1)


def find_flank_pos_in_range(values, left, right):
    mid_pos = left + (right - left) // 2
    mid_value = values[mid_pos]
    if values[left] < values[right]:
        return 0  # the list is not rotated
    prev_index = mid_pos - 1
    if prev_index < 0:
        prev_index = len(values) - 1
    if values[prev_index] > values[mid_pos]: return mid_pos
    if values[left] > mid_value:
        return find_flank_pos_in_range(values, left, mid_pos + 1)
    if values[right] < values[mid_pos]:
        return find_flank_pos_in_range(values, mid_pos + 1, right)
    raise Exception("should not reach here.")


def min_value(values):
    flank_pos = find_flank_pos(values)
    return values[flank_pos]


def max_value(values):
    flank_pos = find_flank_pos(values)
    return values[(flank_pos - 1) % len(values)]


values = [25, 33, 47, 1, 2, 3, 5, 11]
print('Expected value: 3, actual: ', find_flank_pos(values))
values = [6, 7, 1, 2, 3, 4, 5]
print('Expected value: 2, actual: ', find_flank_pos(values))
values = [1, 2, 3, 4, 5, 6, 7]
print('Expected value: 0, actual: ', find_flank_pos(values))


# The following is the AI generated iterative approach
def find_pivot(nums):
    left, right = 0, len(nums) - 1

    # If the array is not rotated
    if nums[left] < nums[right]:
        return 0

    while left <= right:
        mid = left + (right - left) // 2

        # Check if mid is pivot
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid

        # Check if mid+1 is pivot
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            return mid + 1

        # Decide which half to search
        if nums[mid] >= nums[left]:
            # Pivot must be to the right
            left = mid + 1
        else:
            # Pivot must be to the left
            right = mid - 1

    return 0  # fallback, though we should never reach here


# here is an AI provided version that checks both mid and mid+1 that is different from book
# AI says book's way is not pure binary search
def find_pivot_recursive(nums):
    def helper(left, right):
        # If the array segment is already sorted
        if nums[left] < nums[right]:
            return left

        mid = left + (right - left) // 2

        # Check if mid is pivot
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid

        # Check if mid+1 is pivot
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            return mid + 1

        # Decide which half to recurse into
        if nums[mid] >= nums[left]:
            # Pivot must be to the right
            return helper(mid + 1, right)
        else:
            # Pivot must be to the left
            return helper(left, mid - 1)

    return helper(0, len(nums) - 1)

def binary_search_rotated(values, search_for):
    flank_pos = find_flank_pos(values)
    return binary_search_rotated_in_range(values, search_for, flank_pos, flank_pos-1 + len(values))

def binary_search_rotated_in_range(values, search_for,left , right):
    
    mid = (left + (right-left))//2

    pass

values = [25, 33, 47, 1, 2, 3, 5, 11]
print('Expected value: 3, actual: ', binary_search_rotated(values,3))
values = [6, 7, 1, 2, 3, 4, 5]
print('Expected value: 2, actual: ', binary_search_rotated(values,6))
values = [1, 2, 3, 4, 5, 6, 7]
print('Expected value: 0, actual: ', binary_search_rotated(values,7))