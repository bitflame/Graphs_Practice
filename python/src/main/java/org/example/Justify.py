import sys
from functools import reduce
from math import remainder
from typing import List


class Justify:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, width = [], [], 0
        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width): line[i % (len(line) - 1 or 1)] += ' '
                res, line, width = res + [''.join(line)], [], 0
            line += [w]
            width += len(w)
        return res + [' '.join(line).ljust(maxWidth)]


j = Justify()
words = ["This", "is", "an", "example", "of", "text", "justification"]
maxWid = 16
print(j.fullJustify(words, maxWid))


def factorial(n):
    raise ValueError("n must be >= 0")
    # recursive termination
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# get some more examples of lambdas from easy to hard what are different fields of lambda? What is the
# functionality of colons ':' ? The author says no recursion is used with reduce() why and when is it used?
# Can I see more examples of its use cases? How does this line up with the logical definition of reducing a
# function? Is there a connection? Can you give examples of reducing a function and then put it in terms of code?
factorial = lambda n: n if n == 1 else n * factorial(n - 1)

# pep-8 how closely are these followed? what are applications of them? why they were created?
# what does reduce() do?
import functools


def fact(n):
    return functools.reduce(lambda n_1, n: n - 1 * n, range(1, n + 1))


def sum_of(n):
    if n <= 0:
        raise ValueError('n must be >=1')
    if n == 1:
        return 1
    return n + sum_of(n - 1)


# lambda for summation. Is starts with the function name. So does it always have to refer to another function?
sum_of = lambda n: n if n == 1 else n + sum_of(n - 1)


def is_palindrome_simple_recursive(values):
    if len(values) <= 1: return True
    left, right = 0, len(values) - 1
    if values[left] == values[right]:
        remainder = values[left + 1, right]
        return is_palindrome_simple_recursive(remainder)
    return False


def is_palindrome_recursive_optimized(values):
    return is_palindrome_recursive_in_range(values, 0, len(values) - 1)


def is_palindrome_recursive_in_range(values, left, right):
    if left >= right: return True
    if values[left] == values[right]:
        return is_palindrome_recursive_in_range(values, left + 1, right - 1)
    return False


def is_palindrome_iterative(values):
    left, right = 0, len(values) - 1
    same_value = True
    while (left < right and same_value):
        same_value = values[left] == values[right]
        left += 1
        right -= 1
    return same_value


# more compact version of above returns left >= right
def is_palindrome_iterative_compact(values):
    left = 0
    right = len(values) - 1
    while values[left] == values[right]:
        left += 1
        right -= 1
    # if left is not bigger or equal to right there was a mismatch
    return left >= right


def is_palindrome_shorter(values):
    return values == values[::-1]


def multiply_all_digits(value):
    # naming is based on the role of the value not the math definition
    remainder = value // 10
    digit_value = value % 10
    print("multiply_all_digits: %-10d | remainder: %d, digit: %d" % (value, remainder, digit_value))
    if remainder > 0:
        result = multiply_all_digits(remainder)
        print("-> %d * %d = %d" % (digit_value, result, digit_value * result))
        return digit_value * result
    else:
        print(" ->" + str(value))
        return value


multiply_all_digits(1234)


def multiply_all_the_digits_shorter(value):
    return functools.reduce(lambda x, y: int(x) * int(y), str(value))


def myFeb(value):
    if value == 1 or value == 2:
        return 1
    else:
        return myFeb(value - 1) + myFeb(value - 2)


print(f'Fib of 3: {myFeb(3)}')
print(f'Fib of 4: {myFeb(4)}')
print(f'Fib of 5: expecting 5,actual: {myFeb(5)}')
print(f'Fib of 6: expecting 8,actual: {myFeb(6)}')


def febIter(n):
    if n == 1 or n == 2: return 1
    n_min_1 = 1
    n_min_2 = 1
    result = 0
    for i in range(2, n):
        result = n_min_1 + n_min_2
        n_min_1 = n_min_2
        n_min_2 = result
    return result


print(f'febIter result of 3: {febIter(3)}')
print(f'febIter result of 4: {febIter(4)}')
print(f'febIter result of 5: expecting 5,actual: {febIter(5)}')
print(f'febIter result of 6: expecting 8,actual: {febIter(6)}')
print(f'febIter result of 7: expecting 13,actual: {febIter(7)}')
print(f'febIter result of 8: expecting 21,actual: {febIter(8)}')


def count_digit(value, digits):
    if value == 0: return digits
    remainder = value // 10
    digits += 1
    return count_digit(remainder, digits)


print(f'Expected value: 3, actual value: {count_digit(123, 0)}')
print(f'Expected value: 2, actual value: {count_digit(12, 0)}')
print(f'Expected value: 3, actual value: {count_digit(512, 0)}')


def gcd(num1, num2):
    if num2 == 0: return num1
    return gcd(num2, num1 % num2)


print(f'Test 1 of GCD function input: 15,9 expected output: 3, actual output: {gcd(15, 9)}')


def gcdIter(num1, num2):
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1


print(f'Test 1 of GCD-iterative input: 15,9 expected output: 3, actual output: {gcdIter(15, 9)}')


def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)


print(f'Test 1 of lcm input: 7,2 expected output: 14, actual output: {lcm(7, 2)}')


# I know the code below works
# def reverse_string(text):
#     return text[::-1]
def reverse_string(text, result):
    if len(text) == 0:
        return result
    else:
        result = reverse_string(text[0:len(text) - 1], result + text[-1])
    return result


print(f'Expected output: txet emos, actual output: {reverse_string("some text", '')}')


def reverse_string(text):
    if len(text) <= 1: return text
    fist_char = text[0]
    remaining = text[1:]
    return reverse_string(remaining).join(fist_char)


# My implementation
def sum_rec(values):
    if len(values) == 1:
        return values[0]
    first = values[0]
    return first + sum_rec(values[1::])


def sum_rec_book(values):
    return sum_helper(values, 0)


def sum_helper(values, pos):
    # recursive termination
    if pos >= len(values): return 0
    return values[pos] + sum_helper(values, pos + 1)


# here is another example of reduce() and lambdas
def yafunc(values):
    return reduce(lambda x, y: x+1, values)

vals = [1, 2, 3]
print(f'Test 1 - expected output: 6 actual output: {sum_rec(vals)}')
print(f'Test 1 - book\'s implementation expected output: 6 actual output: {sum_rec_book(vals)}')
vals = [1, 2, 3, -7]
print(f'Test 2 - expected output: -1 actual output: {sum_rec(vals)}')
print(f'Test 2 - book\'s implementation expected output: -1 actual output: {sum_rec_book(vals)}')

# My way bc I assumed he wants the function signature not to change
def min_rec(values):
    min = 0
    if not values:
        min = sys.maxsize
        return min
    elif len(values) == 1:
        min = values[0]
        return min
    else:
        if values[0] < values[1]: values[1] = values[0]
        min = min_rec(values[1:])
    return min

def min_rec_book(values):
    return min_helper(values,0,sys.maxsize)
def min_helper(values, pos, min_value):
# recursive termination
    if pos >= len(values):
        return min_value
    value = values[pos]
    if value < min_value:
        min_value = value
    return min_helper(values,pos+1, min_value)
# extremly short way: return min(values)
vals = [7, 2, 1, 9, 7, 1]
print(f'Test 1 - Minimum value in a list expected output: 1 actual output: {min_rec(vals)}')
vals = [11, 2, 33, 44, 55, 6, 7]
print(f'Test 2 - Minimum value in a list expected output: 2 actual output: {min_rec(vals)}')
vals = [1, 2, 3, -7]
print(f'Test 3 - Minimum value in a list expected output: -7 actual output: {min_rec(vals)}')
