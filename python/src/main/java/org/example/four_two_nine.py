def contains_rotation(str1, str2):
    n = len(str2)
    m = len(str1)
    for i in range(m):
        for j in range(n):
            if str1[i] != str2[j]:
                break
            elif i == j:
                i += 1
            if j == n - 1:
                return True
    return False


print(f'Test 1- Expected output: True, actual output: {contains_rotation('ABCD', 'ABC')}')
print(f'Test 2- Expected output: True, actual output: {contains_rotation('ABCDEF', 'EFAB')}')
print(f'Test 3- Expected output: True, actual output: {contains_rotation('ABCDEF', 'efAB')}')
print(f'Test 3- Expected output: True, actual output: {contains_rotation('ABABABABCAB', 'ABC')}')
print(f'Test 4- Expected output: False, actual output: {contains_rotation('ABCDEF', 'EFAD')}')
