# ch four stuff write a function that checks a number to be binary, to run faster you can hard code the
# ascii values of 1 and 0 so you don't have to look it up every time  also, you can use a variable for the
# ascii of the digit so you don't have to call it twice
from curses.ascii import isalpha


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
        if not (int(num) == 1 or int(num) == 0) or isalpha(num):
            return False
    return True


print(f'Test 1 - expected output: True, actual output: {is_bin('1100')}')
print(f'Test 2 - expected output: False, actual output: {is_bin('1127')}')
print(f'Test 3 - expected output: True, actual output: {is_bin('11')}')
print(f'Test 4 - expected output: True, actual output: {is_bin('00')}')
print(f'Test 5 - expected output: True, actual output: {is_bin('1')}')
print(f'Test 6 - expected output: True, actual output: {is_bin('0')}')
print(f'Test 7 - expected output: False, actual output: {is_bin('A')}')
