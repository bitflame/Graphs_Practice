def check_no_duplicate_chars(text):
    seen = [0] * 256
    for c in text:
        if seen[ord(c.lower())] == 0:
            seen[ord(c.lower())] = 1
        else:
            return False
    return True


print(f'Expected output: False, actual output: {check_no_duplicate_chars('Otto')}')
print(f'Expected output: False, actual output: {check_no_duplicate_chars('Adrian')}')
print(f'Expected output: True, actual output: {check_no_duplicate_chars('Micha')}')
print(f'Expected output: True, actual output: {check_no_duplicate_chars('ABCDEFG')}')


# here is the set() version of the code
def no_dup(text):
    seen = set()
    for i in text.lower():
        if i in seen:
            return False
        seen.add(i)
    return True


# or even better
def n_dup(text):
    t = text.lower()
    return len(t) == len(set(t))
