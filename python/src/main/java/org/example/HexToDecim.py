def hex_to_dec(number):
    map = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    result = 0
    for index, num in enumerate(reversed(number)):
        if num.isalpha():
            result += map.get(num.lower()) * 16 ** index
        else:
            result += int(num) * 16 ** index
    return result


print(f'expected output: 15, actual output: {hex_to_dec('f')}')
print(f'expected output: 14, actual output: {hex_to_dec('e')}')
print(f'expected output: 13, actual output: {hex_to_dec('d')}')
print(f'expected output: 13, actual output: {hex_to_dec('D')}')
print(f'expected output: 12, actual output: {hex_to_dec('c')}')
print(f'expected output: 11, actual output: {hex_to_dec('b')}')
print(f'expected output: 0, actual output: {hex_to_dec('0')}')
print(f'expected output: 255, actual output: {hex_to_dec('ff')}')
