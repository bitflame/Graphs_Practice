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
