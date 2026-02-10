# from book Python Challenges by Micahel Inden
def calc_permutation(text):
    # recursive termination
    if is_blank(text) or len(text) == 1:
        return {text}
    combinations = set()
    # extract i-th character as new first character
    for i, new_first in enumerate(text):
        permutations = calc_permutation(text[0:i] + text[i + 1:])
        # adding teh extracted character to all partial solutions
        for perm in permutations:
            combinations.add(new_first + perm)
    return combinations


def is_blank(text):
    return not (text and text.strip())


letters = 'ABC'
print(f'Test 2- input: ABC, expecting: ABC, ACB, BAC, BCA, CAB, CBA, actual output: {calc_permutation(letters)}')
letters = 'AB'
print(f'Test 1- input: ABC, expecting: AB, BA, actual output: {calc_permutation(letters)}')
letters = [letters[0] + letters[1::], letters[1::] + letters[0]]
print(letters)


# here is an optimized version of the above
def cal_permutations_mini_opt(text):
    return __calc_permutations_mini_opt_helper(text, "")


def __calc_permutations_mini_opt_helper(remaining, prefix):
    # recursive terminations
    if len(remaining) == 0:
        return {prefix}
    candidates = set()

    for i, current_char in enumerate(remaining):
        new_prefix = prefix + current_char
        new_remaining = remaining[0:i] + remaining[i + 1:]

        # recursive descent
        candidates.update(__calc_permutations_mini_opt_helper(new_remaining, new_prefix))
    return candidates


letters = 'ABC'
print(
    f'Test 1- Permutation optimized input: ABC, expecting: ABC, ACB, BAC, BCA, CAB, CBA, actual output: {cal_permutations_mini_opt(letters)}')


def myMethod(chars):
    if len(chars) == 1: return chars
    combinations = set()
    for i, newChar in enumerate(chars):
        permutations = myMethod(chars[:i] + chars[i + 1:])
        for permutation in permutations:
            combinations.add(newChar + permutation)
    return combinations


print(f'{myMethod('ABC')}')
# example of using the itertools function
import itertools


def cal_permutation_built_in(text):
    result_tuples = list(itertools.permutations(text))
    return {"".join(tuple) for tuple in result_tuples}


for per in itertools.permutations('ABC'):
    print(per)

print(cal_permutation_built_in('ABC'))
