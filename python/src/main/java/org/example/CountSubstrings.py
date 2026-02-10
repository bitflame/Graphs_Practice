# My code
def count_substrings(text, value_to_find):
    m = len(text)
    n = len(value_to_find)
    t = 0
    p = 0
    matches = 0
    while t < len(text) and p < len(value_to_find):
        if text[t]==value_to_find[p]:
            p+=1
            t+=1
            if p == n:
                matches+=1
                text=text[:t-p]+text[t:]
                t = t - p
                p = 0
        else: t+=1
    return matches


print(f'Test 1 - expected output: 3, actual output: {count_substrings('xhixhix', 'x')}')
print(f'Test 2 - expected output: 2, actual output: {count_substrings('xhixhix', 'hi')}')
print(f'Test 3 - expected output: 1, actual output: {count_substrings('mic', 'mic')}')
print(f'Test 4 - expected output: 0, actual output: {count_substrings('xhoxhox', 'hi')}')
print(f'Test 5 - expected output: 2, actual output: {count_substrings('xxxxyz', 'xx')}')

