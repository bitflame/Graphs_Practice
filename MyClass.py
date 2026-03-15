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
    pos1, pos2 = len(str_one) - 1, len(str_two) - 1
    return distance_helper(str_one, str_two, pos1, pos2)


def distance_helper(str_one, str_two, pos1, pos2):
    if pos1 < 0:
        return pos2 + 1
    if pos2 < 0:
        return pos1 + 1
    if str_one[pos1] == str_two[pos2]:
        return distance_helper(str_one, str_two, pos1 - 1, pos2 - 1)
    else:
        insert_in_first = distance_helper(str_one, str_two, pos1, pos2 - 1)
        delete_in_first = distance_helper(str_one, str_two, pos1 - 1, pos2)
        change = distance_helper(str_one, str_two, pos1 - 1, pos2 - 1)
    return 1 + min(insert_in_first, delete_in_first, change)


st_one = 'Micha'
st_two = 'Michael'
print(f'Test 1 - expected answer: 2, actual answer: {get_dist(st_one, st_two)}')
print(f'Test 2 - expected answer: 2, actual answer: {get_dist(st_two, st_one)}')
st_one = 'rapple'
st_two = 'tables'
print(f'Test 3 - expected answer: 4, actual answer: {get_dist(st_two, st_one)}')
print(f'Test 4 - expected answer: 4, actual answer: {get_dist(st_one, st_two)}')
st_one = 'a'
st_two = 'b'
print(f'Test 5 - expected answer: 1, actual answer: {get_dist(st_two, st_one)}')
print(f'Test 6 - expected answer: 1, actual answer: {get_dist(st_one, st_two)}')
st_one = 'aa'
st_two = 'bb'
print(f'Test 7 - expected answer: 2, actual answer: {get_dist(st_two, st_one)}')
print(f'Test 8 - expected answer: 2, actual answer: {get_dist(st_one, st_two)}')


def get_dist_memo(str_one, str_two):
    pos1, pos2 = len(str_one) - 1, len(str_two) - 1
    return distance_helper_memo(str_one, str_two, pos1, pos2, {})


def distance_helper_memo(str_one, str_two, pos1, pos2, values):
    if pos1 < 0:
        return pos2 + 1
    if pos2 < 0:
        return pos1 + 1
    if (pos1, pos2) in values:
        # print('cached value provided.')
        return values[(pos1, pos2)]
    if str_one[pos1] == str_two[pos2]:
        result = distance_helper_memo(str_one, str_two, pos1 - 1, pos2 - 1, values)
    else:
        insert_in_first = distance_helper_memo(str_one, str_two, pos1, pos2 - 1, values)
        delete_in_first = distance_helper_memo(str_one, str_two, pos1 - 1, pos2, values)
        change = distance_helper_memo(str_one, str_two, pos1 - 1, pos2 - 1, values)
        result = 1 + min(insert_in_first, delete_in_first, change)
    values[(pos1, pos2)] = result
    return result


st_one = 'Micha'
st_two = 'Michael'
print(f'Test 1 - expected answer: 2, actual answer: {get_dist_memo(st_one, st_two)}')
print(f'Test 2 - expected answer: 2, actual answer: {get_dist_memo(st_two, st_one)}')
st_one = 'rapple'
st_two = 'tables'
print(f'Test 3 - expected answer: 4, actual answer: {get_dist_memo(st_two, st_one)}')
print(f'Test 4 - expected answer: 4, actual answer: {get_dist_memo(st_one, st_two)}')
st_one = 'a'
st_two = 'b'
print(f'Test 5 - expected answer: 1, actual answer: {get_dist_memo(st_two, st_one)}')
print(f'Test 6 - expected answer: 1, actual answer: {get_dist_memo(st_one, st_two)}')
st_one = 'aa'
st_two = 'bb'
print(f'Test 7 - expected answer: 2, actual answer: {get_dist_memo(st_two, st_one)}')
print(f'Test 8 - expected answer: 2, actual answer: {get_dist_memo(st_one, st_two)}')
