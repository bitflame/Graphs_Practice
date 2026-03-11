def both_vals_should_be_pos(binary_func):
    def helper(val1, val2):
        if type(val1) == int and val1 > 0 and type(val2) == int and val2 > 0:
            return binary_func(val1, val2)
        else:
            raise ValueError('Both parameters have to be pos.')

    return helper


@both_vals_should_be_pos
def adding_func(val1, val2):
    return val1 + val2


@both_vals_should_be_pos
def subtract_func(val1, val2):
    return val1 - val2


print(f'expected value: 3, actual: {subtract_func(5, 2)}')
print(f'expected value: 7, actual: {adding_func(5, 2)}')


def check_sign_of_arguments(unary_func):
    def helper(n):
        if n <= 0:
            raise ValueError('The argument should be positive.')
        else:
            return unary_func(n)

    return helper


@check_sign_of_arguments
def my_factorial(n):
    if n == 1: return 1
    return n * my_factorial(n - 1)


print(my_factorial(3))
