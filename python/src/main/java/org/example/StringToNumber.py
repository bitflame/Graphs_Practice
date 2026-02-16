def str_to_octal(num_txt):
    result = 1
    M = len(num_txt)
    for i in range(M - 1, 1, -1):
        result *= 8
        result += ord(num_txt[i]) - 48
    return result


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
            if num_txt[counter] == '0' and num_txt[counter + 1] == 'o':
                result = str_to_octal(num_txt)
                return result
            continue
        elif num_txt[counter] not in my_digits:
            return ValueError('The must contain numbers or negative sign. Nothing else!')
        elif num_txt[counter] == '0' and num_txt[counter + 1] == 'o':
            result = str_to_octal(num_txt)
            return -result if isNeg else result
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
print(f'Test 8 - input: 0o77, expected output: 63 actual output: {str_to_num('0o77')}')
print(f'Test 9 - input: -0o77, expected output: -63 actual output: {str_to_num('-0o77')}')
print(f'Test 10 - input: +0o77, expected output: -63 actual output: {str_to_num('+0o77')}')
print(f'Test 11 - input: +0o77, expected output: -63 actual output: {str_to_num('+0o77')}')
print(f'Test 12 - input: -0o123, expected output: -83 actual output: {str_to_num('-0o123')}')
print(f'Test 13 - input: 0o123, expected output: 83 actual output: {str_to_num('0o123')}')
