def binary_to_decimal(number):
    result, factor = 0, 1
    for index, digit in enumerate(reversed(number)):
        if digit == '1':
            result += int(digit) * pow(2, index)
    return result


print(f'Test 1 - expected output: 0, actual output: {binary_to_decimal('0')}')
print(f'Test 2 - expected output: 1, actual output: {binary_to_decimal('1')}')
print(f'Test 3 - expected output: 2, actual output: {binary_to_decimal('10')}')
print(f'Test 4 - expected output: 3, actual output: {binary_to_decimal('11')}')
print(f'Test 5 - expected output: 4, actual output: {binary_to_decimal('100')}')
