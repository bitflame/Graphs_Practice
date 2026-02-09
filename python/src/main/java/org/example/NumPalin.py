


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