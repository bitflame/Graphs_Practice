# ch four stuff write a function that checks a number to be binary, to run faster you can hard code the
# ascii values of 1 and 0 so you don't have to look it up every time and you can use a variable for the
# ascii of the digit so you don't hav e to call it twice
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
