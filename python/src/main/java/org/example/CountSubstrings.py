# My code
def count_substrings_mine(text, value_to_find):
    m = len(text)
    n = len(value_to_find)
    t = 0
    p = 0
    matches = 0
    while t < len(text) and p < len(value_to_find):
        if text[t] == value_to_find[p]:
            p += 1
            t += 1
            if p == n:
                matches += 1
                text = text[:t - p] + text[t:]
                t = t - p
                p = 0
        else:
            t += 1
    return matches


print(f'Test 1 - expected output: 3, actual output: {count_substrings_mine('xhixhix', 'x')}')
print(f'Test 2 - expected output: 2, actual output: {count_substrings_mine('xhixhix', 'hi')}')
print(f'Test 3 - expected output: 1, actual output: {count_substrings_mine('mic', 'mic')}')
print(f'Test 4 - expected output: 0, actual output: {count_substrings_mine('xhoxhox', 'hi')}')
print(f'Test 5 - expected output: 2, actual output: {count_substrings_mine('xxxxyz', 'xx')}')


def count_substrings(text, value_to_find):
    # recursive termination
    if len(text) < len(value_to_find):
        return 0
    count = 0
    remaining = ""
    # does text start with search string?
    if text.startswith(value_to_find):
        # hit: continue the search for the found
        # term: after the occurrence
        remaining = text[len(value_to_find):]
        count = 1
    else:
        # remove the first character and search again
        remaining = text[1:]
    return count_substrings(remaining, value_to_find) + count


print(f'Test 1 - expected output: 3, actual output: {count_substrings('xhixhix', 'x')}')
print(f'Test 2 - expected output: 2, actual output: {count_substrings('xhixhix', 'hi')}')
print(f'Test 3 - expected output: 1, actual output: {count_substrings('mic', 'mic')}')
print(f'Test 4 - expected output: 0, actual output: {count_substrings('xhoxhox', 'hi')}')
print(f'Test 5 - expected output: 2, actual output: {count_substrings('xxxxyz', 'xx')}')


def myMethod(text, pattern):
    if len(text) < len(pattern): return 0
    count = 0
    remaining = ""
    if text.startswith(pattern):
        remaining = text[len(pattern):]
        count += 1
    else:
        remaining = text = text[1:]
    return myMethod(remaining, pattern) + count


print(f'Test 1 - MyMethod expected output: 3, actual output: {myMethod('xhixhix', 'x')}')
print(f'Test 2 - MyMethod expected output: 2, actual output: {myMethod('xhixhix', 'hi')}')
print(f'Test 3 - MyMethod expected output: 1, actual output: {myMethod('mic', 'mic')}')
print(f'Test 4 - MyMethod expected output: 0, actual output: {myMethod('xhoxhox', 'hi')}')
print(f'Test 5 - MyMethod expected output: 2, actual output: {myMethod('xxxxyz', 'xx')}')


# improved version...
def count_substrings_v2(text, value_to_find):
    # recursive termination
    if len(text) < len(value_to_find): return 0
    count = 1 if text.startswith(value_to_find) else 0
    remaining = text[1:]
    # recursive descent
    count_substrings_v2(remaining) + count


# a problem with the above method is generation of new strings by slice, which the following prevents...
def count_substrings_optimized(text, value_to_find):
    return count_substrings_helper(text, value_to_find, 0)


def count_substrings_helper(text, value_to_find, left):
    if len(text) - left < len(value_to_find):
        return 0
    count = 1 if text.startswith(value_to_find, left) else 0
    if text.startswith(value_to_find, left):
        left += len(value_to_find)
    else:
        left += 1
    return count_substrings_helper(text, value_to_find, left) + count

# built in Python utilities to accomplish the same task

print('xhixhix'.count('x'))
print('xhixhix'.count('hi'))
print('mic'.count('mic'))
print('hahah'.count('ho'))
print('xxxxyz'.count('xx'))