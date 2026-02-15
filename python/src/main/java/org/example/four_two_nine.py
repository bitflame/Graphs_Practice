from zoneinfo import reset_tzpath


def contains_rotation(str1, str2):
    n = len(str2)
    m = len(str1)
    if m < n:
        return False
    elif m == 0 and n == 0:
        return True
    elif m == 0 and n > 0 or m > 0 and n == 0:
        return False
    for i in range(m):
        for j in range(n):
            if str1[i].lower() != str2[j].lower():
                break
            elif str1[i] == str2[j]:
                i += 1
            if j == n - 1:
                return True
    return False


def fixed_version_of_above(str1, str2):
    n = len(str2)
    m = len(str1)
    if m != n: return False
    if m == 0:
        return True
    for start in range(m):
        match = True
        for j in range(n):
            if str1[(start + j) % m] != str2[j]:
                match = False
                break
        if match:
            return True
    return False


def method_two(str1, str2):
    m, n = len(str1), len(str2)
    if m == 0 and n==0: return True
    if m == 0 : return False
    if n == 0: return True
    if n > m: return False
    str1 = str1.lower()
    str2 = str2.lower()
    return str2 in str1 + str1


print(f'Test 1- Expected output: True, actual output: {method_two('ABCD', 'ABC')}')
print(f'Test 2- Expected output: True, actual output: {method_two('ABCDEF', 'EFAB')}')
print(f'Test 3- Expected output: True, actual output: {method_two('ABCDEF', 'efAB')}')
print(f'Test 4- Expected output: True, actual output: {method_two('ABABABABCAB', 'ABC')}')
print(f'Test 5- Expected output: False, actual output: {method_two('ABCDEF', 'EFAD')}')
print(f'Test 6- Expected output: True, actual output: {method_two('aaaaa', 'aaa')}')
print(f'Test 7- Expected output: False, actual output: {method_two('abc', 'abcd')}')
print(f'Test 8- Expected output: True, actual output: {method_two('abcde', 'eabcd')}')
print(f'Test 9- Expected output: False, actual output: {method_two('abcde', 'eabcf')}')
print(f'Test 10- Expected output: False, actual output: {method_two('', 'a')}')
print(f'Test 11- Expected output: True, actual output: {method_two('', '')}')
