def translate_vowels(text, replacement):
    vowels = {'a', 'e', 'i', 'o', 'u', }
    result = []
    for curr in text:
        if curr.lower() in vowels:
            result.append(replacement)
        else:
            result.append(curr)
    return ''.join(result)


print(f'expected output: g??d, actual output: {translate_vowels('guide', '?')}')
print(f'expected output: l-wnm-w-r, actual output: {translate_vowels('lawnmower', '-')}')
print(f'expected output: q z, actual output: {translate_vowels('quiz', '_')}')
print(f'expected output: lwnmwr, actual output: {translate_vowels('lawnmower', '')}')
