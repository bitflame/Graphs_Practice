import functools


def decorate_with_memo_shorter(func):
    lookup_map = dict()

    @functools.wraps(func)
    def helper(*args):
        if args not in lookup_map:
            lookup_map[args] = func(*args)
        return lookup_map[args]

    return helper


@decorate_with_memo_shorter
def pascal_rec(row, col):
    if col == 1 and row == 1:
        return 1
    if col == 1 or col == row:
        return 1
    return pascal_rec(row - 1, col) + pascal_rec(row - 1, col - 1)


def print_pascal_rec(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(pascal_rec(row, col), end=' ')

        print()


print_pascal_rec(3)


def check_argument_is_positive_integer(unary_func):
    def helper(n):
        if type(n) == int and n > 0:
            return unary_func(n)
        else:
            raise ValueError('The variables you pass to function should be positive.')

    return helper


def another_decorator_function(func):
    @functools.wraps(func)
    def helper(*args):
        for item in enumerate(args):
            if item > 0:
                return func(*args)
            else:
                raise ValueError('All numbers should be positive.')
        return helper


# @decorate_with_memo_shorter
@ functools.lru_cache(maxsize=None)
@check_argument_is_positive_integer
def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

print(fib_rec.cache_info())
print(fib_rec(5))
print(fib_rec.cache_info())

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
