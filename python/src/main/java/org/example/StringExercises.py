# ch four stuff
def is_binary_number(number):
    if not number: return False
    for digit in number:
        if digit != '1' or digit != '0':
            return False
    return True


print(is_binary_number('1127'))
