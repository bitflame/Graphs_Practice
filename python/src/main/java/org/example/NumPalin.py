
def power_of_ten(number):
    count = 0
    while number > 0:
        number //=10
        count+=1
    return count

def is_pal_num(number):
    if number<10: return True
    factor = power_of_ten(number)-1
    divisor = int(pow(10,factor))
    if number < divisor*10:
        left_number = number//divisor
        right_number = number%10
        remaining_number = (number//10) % (divisor//10)
        return left_number==right_number and is_pal_num(remaining_number)
    return False

print(f'expected output: True, actual output:{is_pal_num(737)}')
print(f'expected output: False, actual output:{is_pal_num(13)}')
print(f'expected output: True, actual output:{is_pal_num(4774)}')

# My attempt of validating I can solve the problem
def myMethod(num):
    if num < 10: return True
    divisor = calDivisor(num)
    left_digit = num // divisor -1
    right_digit = num % 10
    remaining_digits = (num//10)%(divisor//10)
    return right_digit==left_digit and myMethod(remaining_digits)


def calDivisor(num):
    counter=0
    while num!=0:
        num//=10
        counter+=1
    return counter

print(f'Test 1 - input: 737, expected output: True, actual output: {myMethod(737)}')
print(f'Test 2 - input: 1, expected output: True, actual output: {myMethod(1)}')
print(f'Test 3 - input: 44247, expected output: False, actual output: {myMethod(44247)}')