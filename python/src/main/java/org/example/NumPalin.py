import pytest


def power_of_ten(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def is_pal_num(number):
    if number < 10: return True
    factor = power_of_ten(number) - 1
    divisor = int(pow(10, factor))
    if number < divisor * 10:
        left_number = number // divisor
        right_number = number % 10
        remaining_number = (number // 10) % (divisor // 10)
        return left_number == right_number and is_pal_num(remaining_number)
    return False


print(f'expected output: True, actual output:{is_pal_num(737)}')
print(f'expected output: False, actual output:{is_pal_num(13)}')
print(f'expected output: True, actual output:{is_pal_num(4774)}')


# My attempt of validating I can solve the problem
def myMethod(num):
    if num < 10: return True
    divisor = pow(10, calDivisor(num) - 1)
    left_digit = num // divisor
    right_digit = num % 10
    remaining_digits = (num // 10) % (divisor // 10)
    return right_digit == left_digit and myMethod(remaining_digits)


def calDivisor(num):
    counter = 0
    while num != 0:
        num //= 10
        counter += 1
    return counter


print(f'Test 1 - input: 737, expected output: True, actual output: {myMethod(737)}')
print(f'Test 2 - input: 1, expected output: True, actual output: {myMethod(1)}')
print(f'Test 3 - input: 44247, expected output: False, actual output: {myMethod(44247)}')
print(f'Test 4 - input: 13, expected output: False, actual output: {myMethod(13)}')
print(f'Test 5 - input: 4774, expected output: False, actual output: {myMethod(4774)}')


# optimized method
def optimized_num_pal(number):
    return helper(number, 0, number)


def helper(original_num, current_value, remaining_val):
    if original_num == current_value: return True
    if remaining_val < 0: return False
    last_digit = remaining_val % 10
    new_curr_val = current_value * 10 + last_digit
    new_remaining_val = remaining_val // 10
    return helper(original_num, new_curr_val, new_remaining_val)


print(f'Test 1 optimized_num_pal() input: 737, expected output: True, actual output: {optimized_num_pal(737)}')
print(f'Test 2 optimized_num_pal() input: 13, expected output: False, actual output: {optimized_num_pal(13)}')
@pytest.mark.parametrize("number, expected", [(7,True),(13, False),(171, True),(47742, False),(123321,True),(1234554321,True)])
def test_is_number_palindrome(number, expected):
    assert optimized_num_pal(number)== expected
