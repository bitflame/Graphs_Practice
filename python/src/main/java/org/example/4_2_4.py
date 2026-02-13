def is_palindrome(text):
    first, last = 0, len(text) - 1
    while first < last:
        if text[first].lower() != text[last].lower():
            return False
        first += 1
        last -= 1
    return True


print(f'{is_palindrome('Otto')}')
print(f'{is_palindrome('ABCBX')}')
print(f'{is_palindrome('ABCXcba')}')