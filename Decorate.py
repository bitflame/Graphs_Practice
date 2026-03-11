def calc_pascal(row, col):
    if row == 1 and col == 1:
        return 1
    if col == 1 or col == row:
        return 1
    return calc_pascal(row - 1, col) + calc_pascal(row - 1, col - 1)


def calc_pascal_memoized(row, col):
    return calc_pascal_helper(row, col, {})


def calc_pascal_helper(row, col, lookup_table):
    key = (row, col)
    result = 0
    if key in lookup_table:
        # print('had a table hit.') For n=10 we have 5 table hits:)
        return lookup_table[key]
    if row == 1 and col == 1:
        return 1
    if col == 1 or col == row:
        return 1
    else:
        result = calc_pascal_helper(row - 1, col, lookup_table) + calc_pascal_helper(row - 1, col - 1, lookup_table)
        lookup_table[key] = result
    return result


def print_pascal(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(calc_pascal_memoized(row, col), end=' ')

        print()

print_pascal(6)


def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n - 1) + (n - 2)


def memoized_febo(n):
    return memoized_febo_helper(n, {})


def memoized_febo_helper(n, dict):
    result = 0
    if n in dict:
        return dict.get(n)
    if n == 1 or n == 0:
        result = 1
    else:
        result = memoized_febo_helper(n - 1, dict) + memoized_febo_helper(n - 2, dict)
    dict[n] = result
    return result


print(memoized_febo(1))
print(memoized_febo(2))
print(memoized_febo(3))
print(memoized_febo(4))


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
