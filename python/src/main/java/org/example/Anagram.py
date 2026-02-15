def is_anagram(str1, str2):
    m = len(str1)
    n = len(str2)
    if m != n:
        return False
    elif m == 0 and m == 0:
        return True
    letters = [0] * 26
    for i, first_car in enumerate(str1):
        letters[ord(first_car.lower()) - 97] += 1
    for j, sec_car in enumerate(str2):
        letters[ord(sec_car.lower()) - 97] -= 1
    for i in letters:
        if i != 0: return False
    return True


print(f'Test 1 - Expected output: True, actual output: {is_anagram('', '')}')
print(f'Test 2 - Expected output: False, actual output: {is_anagram('', 'Toto')}')
print(f'Test 3 - Expected output: False, actual output: {is_anagram('Otto', '')}')
print(f'Test 4 - Expected output: True, actual output: {is_anagram('a', 'a')}')
print(f'Test 5 - Expected output: True, actual output: {is_anagram('Otto', 'Toto')}')
print(f'Test 6 - Expected output: False, actual output: {is_anagram('Ananas', 'Bananas')}')


# faster way is to sort both strings, then return false as soon as you see a mismatch
def sec_attempt(str1, str2):
    m = len(str1)
    n = len(str2)
    if m != n:
        return False
    elif m == 0 and n == 0:
        return True
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())
    for i in range(m):
        if str1[i] != str2[i]: return False
    return True


print(f'Test 1 - Expected output: True, actual output: {sec_attempt('', '')}')
print(f'Test 2 - Expected output: False, actual output: {sec_attempt('', 'Toto')}')
print(f'Test 3 - Expected output: False, actual output: {sec_attempt('Otto', '')}')
print(f'Test 4 - Expected output: True, actual output: {sec_attempt('a', 'a')}')
print(f'Test 5 - Expected output: True, actual output: {sec_attempt('Otto', 'Toto')}')
print(f'Test 6 - Expected output: False, actual output: {sec_attempt('Ananas', 'Bananas')}')


def another_attempt(str1, str2):
    '''different lengths can not be anagrams'''
    if len(str1) != len(str2): return False
    '''sort and compare'''
    return sorted(str1.lower()) == sorted(str2.lower())


print(f'Test 1 - another_attempt Expected output: True, actual output: {another_attempt('', '')}')
print(f'Test 2 - another_attempt  Expected output: False, actual output: {another_attempt('', 'Toto')}')
print(f'Test 3 - another_attempt  Expected output: False, actual output: {another_attempt('Otto', '')}')
print(f'Test 4 - another_attempt  Expected output: True, actual output: {another_attempt('a', 'a')}')
print(f'Test 5 - another_attempt  Expected output: True, actual output: {another_attempt('Otto', 'Toto')}')
print(f'Test 6 - another_attempt  Expected output: False, actual output: {another_attempt('Ananas', 'Bananas')}')
