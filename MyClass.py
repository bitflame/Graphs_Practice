def hanoi(n, source, auxiliary, destination):
    if n <= 1:
        print(source, '->', destination)
    else:
        hanoi(n - 1, source, destination, auxiliary)
        print(source, '->', destination)
        hanoi(n - 1, auxiliary, source, destination)


src = 'A'
aux = 'B'
dest = 'C'
hanoi(3, src, aux, dest)


def get_dist(str_one, str_two):
    len_one, len_two = len(str_one) - 1, len(str_two) - 1
    return distance_helper(str_one, len_one, str_two, len_two, 0)


def distance_helper(str_one, len_one, str_two, len_two, curr_char_index):
    modified_chars = 0
    if curr_char_index > len_one and curr_char_index > len_two:
        return min(len_one, len_two)
    if curr_char_index > len_one and curr_char_index < len_two:
        str_one = str_one + str_two[curr_char_index:]
        return len_two - len_one
    elif curr_char_index > len_two and curr_char_index < len_one:
        str_two = str_two + str_one[curr_char_index:]
        return len_one - len_two
    elif str_one[curr_char_index] == str_two[curr_char_index]:
        modified_chars = distance_helper(str_one, len_one, str_two, len_two, curr_char_index + 1)
    else:
        insert(str_one, curr_char_index, str_two[curr_char_index])
        modified_chars = 1 + min(modified_chars,
                                 distance_helper(str_one, len_one, str_two, len_two, curr_char_index))
        remove(str_one, curr_char_index)
        modified_chars = 1 + min(modified_chars,
                                 distance_helper(str_one, len_one, str_two, len_two, curr_char_index))
        replace(str_one, str_two, curr_char_index)
        modified_chars = 1 + min(modified_chars,
                                 distance_helper(str_one, len_one, str_two, len_two, curr_char_index))
        curr_char_index += 1
    return modified_chars


def insert(target_str, index, additional_char):
    print(f'modified {target_str}')
    target_str = target_str[:index] + additional_char + target_str[index + 1:]
    print(f'to: {target_str}')


def remove(target_str, index):
    print(f'modified {target_str}')
    target_str = target_str[:index] + target_str[index + 1:]
    print(f'to: {target_str}')


def replace(target_str, source_str, index):
    print(f'modified {target_str}')
    target_str[index] = source_str[index]
    print(f'to: {target_str}')


st_one = 'Micha'
st_two = 'Michael'
print(f'Test 1 - expected answer: 2, actual answer: {get_dist(st_one, st_two)}')
print(f'Test 2 - expected answer: 2, actual answer: {get_dist(st_two, st_one)}')
st_one = 'rapple'
st_two = 'tables'
print(f'Test 3 - expected answer: 2, actual answer: {get_dist(st_two, st_one)}')
print(f'Test 3 - expected answer: 2, actual answer: {get_dist(st_one, st_two)}')
