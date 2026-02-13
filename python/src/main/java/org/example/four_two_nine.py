def contains_rotation(str1, str2):
    text_index, pattern_index = 0, 0
    m = len(str1)
    n = len(str2)
    while text_index < m:
        if str1[text_index].lower() == str2[pattern_index].lower():
            if pattern_index == n - 1:
                return True
            text_index += 1
            pattern_index += 1
        else:
            text_index += 1
    return False


print(f'Test 1- Expected output: True, actual output: {contains_rotation('ABCD', 'ABC')}')
