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


def distance_helper(str_one, len_one, str_two, len_two, modified_chars_count):
    if len_one < 0 and len_two < 0:
        return modified_chars_count
    elif len_one < len_two:
        modified_chars_count += 1
        len_two -= 1
    elif len_two < len_one:
        modified_chars_count += 1
        len_one -= 1
    elif str.lower(st_one[len_one]) != str.lower(st_two[len_two]):
        modified_chars_count += 1
        len_one -= 1
        len_two -= 1
    else:
        len_one -= 1
        len_two -= 1
    return distance_helper(str_one, len_one, str_two, len_two, modified_chars_count)


st_one = 'Micha'
st_two = 'Michael'
print(f'Test 1 - expected answer: 2, actual answer: {get_dist(st_one, st_two)}')
print(f'Test 2 - expected answer: 2, actual answer: {get_dist(st_two, st_one)}')
st_one = 'rapple'
st_two = 'tables'
print(f'Test 3 - expected answer: 2, actual answer: {get_dist(st_two, st_one)}')