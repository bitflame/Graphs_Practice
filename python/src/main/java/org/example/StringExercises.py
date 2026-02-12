# ch four stuff write a function that checks a number to be binary, to run faster you can hard code the
# ascii values of 1 and 0 so you don't have to look it up every time  also, you can use a variable for the
# ascii of the digit so you don't have to call it twice


def is_binary_number(number):
    if not number: return False
    for digit in number:
        if not (ord(digit) == ord('1') or ord(digit) == ord('0')):
            return False
    return True


print(f'Test 1 - expected output: True, actual output: {is_binary_number('1100')}')
print(f'Test 2 - expected output: False, actual output: {is_binary_number('1127')}')
print(f'Test 3 - expected output: True, actual output: {is_binary_number('11')}')
print(f'Test 4 - expected output: True, actual output: {is_binary_number('00')}')
print(f'Test 5 - expected output: True, actual output: {is_binary_number('1')}')
print(f'Test 6 - expected output: True, actual output: {is_binary_number('0')}')
print(f'Test 7 - expected output: False, actual output: {is_binary_number('A')}')


# another version of hte above method..
def is_bin(number):
    for num in number:
        if num.isalpha() or not (int(num) == 1 or int(num) == 0):
            return False
    return True


print(f'Test 1 - expected output: True, actual output: {is_bin('1100')}')
print(f'Test 2 - expected output: False, actual output: {is_bin('1127')}')
print(f'Test 3 - expected output: True, actual output: {is_bin('11')}')
print(f'Test 4 - expected output: True, actual output: {is_bin('00')}')
print(f'Test 5 - expected output: True, actual output: {is_bin('1')}')
print(f'Test 6 - expected output: True, actual output: {is_bin('0')}')
print(f'Test 7 - expected output: False, actual output: {is_bin('A')}')
print('The next test will fail:')
# print(f'Test 7 - expected output: Big Fat Failure, actual output: {is_bin(' ')}')

def is_bin_optimized(number):
    for i in number:
        if i not in '10':
            return False
    return True
print(f'Test 1 - expected output: True, actual output: {is_bin_optimized('1100')}')
print(f'Test 2 - expected output: False, actual output: {is_bin_optimized('1127')}')
print(f'Test 3 - expected output: True, actual output: {is_bin_optimized('11')}')
print(f'Test 4 - expected output: True, actual output: {is_bin_optimized('00')}')
print(f'Test 5 - expected output: True, actual output: {is_bin_optimized('1')}')
print(f'Test 6 - expected output: True, actual output: {is_bin_optimized('0')}')
print(f'Test 7 - expected output: False, actual output: {is_bin_optimized('A')}')
print(f'Test 8 - expected output: False, actual output: {is_bin_optimized('!')}')
