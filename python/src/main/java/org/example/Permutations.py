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
