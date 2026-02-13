def remove_dups(text):
    return set(text.lower())


print(f'{remove_dups('bananas')}')


# to preserve the order of the characters...
def new_method(text):
    buffer = [0] * 256
    result = []
    for i, c in enumerate(text):
        idx_lower = ord(c.lower())
        if buffer[idx_lower] == 0:
            buffer[idx_lower] = 1
            result.append(c)
    return result


print(f'Test 1 - input: bananas, expected output: bans, actual output: {new_method('bananas')}')
print(f'Test 2 - input: lalalamama, expected output: lam, actual output: {new_method('lalalamama')}')
print(f'Test 3 - input: MICHAEL, expected output: MICHAEL, actual output: {new_method('MICHAEL')}')
print(f'Test 4 - input: AaBbcCdD, expected output: ABcd, actual output: {new_method('AaBbcCdD')}')


def yet_another_way(text):
    buffer = set()
    result = []
    for c in text:
        key = c.lower()
        if key not in buffer:
            buffer.add(key)
            result.append(c)
    return result


print(f'Test 1 - input: bananas, expected output: bans, actual output: {yet_another_way('bananas')}')
print(f'Test 2 - input: lalalamama, expected output: lam, actual output: {yet_another_way('lalalamama')}')
print(f'Test 3 - input: MICHAEL, expected output: MICHAEL, actual output: {yet_another_way('MICHAEL')}')
print(f'Test 4 - input: AaBbcCdD, expected output: ABcd, actual output: {yet_another_way('AaBbcCdD')}')
