def str_to_num(num_txt):
    my_digits = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    mult = 1
    result = 0
    start = 0
    isNeg = False
    counter = 0
    m = len(num_txt)
    while (counter < m and num_txt[counter] not in my_digits):
        if num_txt[counter] == '-':
            isNeg = True
        elif num_txt[counter] == '+':
            start += 1
            counter += 1
            continue
        elif num_txt[counter] not in my_digits:
            return ValueError('The must contain numbers or negative sign. Nothing else!')
        start += 1
        counter += 1
    for dig in range(m - 1, start - 1, -1):
        if num_txt[dig] not in my_digits:
            return ValueError("Characters are not acceptable.")
        result += my_digits[num_txt[dig]] * mult
        mult *= 10
    return -result if isNeg else result


print(f'Test 1 - input: 123, actual output: {str_to_num('123')}')
print(f'Test 2 - input: -123, actual output: {str_to_num('-123')}')
print(f'Test 3 - input: 7271, actual output: {str_to_num('7271')}')
print(f'Test 4 - input: ABC, expected output is an error message actual output: {str_to_num('ABC')}')
print(f'Test 5 - input: 0123, expected output: 123 actual output: {str_to_num('0123')}')
print(f'Test 6 - input: -0123, expected output: -123 actual output: {str_to_num('-0123')}')
print(f'Test 7 - input: +0123, expected output: 123 actual output: {str_to_num('+0123')}')