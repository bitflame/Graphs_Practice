def reverse(text):
    first, last = 0, len(text)
    if last == 1: return text
    buffer = list(text)
    while first < last:
        buffer[last-1], buffer[first]=buffer[first], buffer[last-1]
        first += 1
        last -= 1
    return "".join(buffer)


text = 'ABCD'
print(reverse(text))
print(f'expected output: DCBA, actual output: {reverse(text)}')
print(f'expected output: OTTO, actual output: {reverse('OTTO')}')
print(f'expected output: RETEP, actual output: {reverse('PETER')}')
