
def is_number_palindrome(number):
    if number < 10: return True
    factor = calc_pow_of_ten(number)
    divisor = int(pow(10,factor))
    if number < divisor * 10:
        left_number = number // divisor
        right_number = number % 10

        # cuts away a leading zero ...
        remaining_number = (number//10) % (divisor//10)
        return left_number == right_number and is_number_palindrome(remaining_number)
    return False

def calc_pow_of_ten(number):
    return count_digits(number)-1

def count_digits(number):
    count = 0
    while number > 0:
        number = number // 10
        count+=1
    return count

print(4226//1000)
print(f'Test 1 - input: 7, expected output: True, actual output: {is_number_palindrome(7)}')
print(f'Test 2 - input: 13, expected output: False, actual output: {is_number_palindrome(13)}')
print(f'Test 3 - input: 171, expected output: True, actual output: {is_number_palindrome(171)}')
print(f'Test 4 - input: 47742, expected output: True, actual output: {is_number_palindrome(4774)}')