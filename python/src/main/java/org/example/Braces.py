from colorama.ansi import clear_line


def check_braces(text):
    return helper(text, len(text))


def helper(text, N):
    if N == 1:
        return False
    elif N == 0:
        return True
    else:
        return helper(text[1:N - 1], N - 2)


print(f'{check_braces('(())')}')
print(f'{check_braces('()()')}')
print(f'{check_braces('(()))')}')
print(f'{check_braces('((())')}')


def attempt_two(text):
    left_counter = 0
    right_counter = 0
    for i, curr in enumerate(text):
        if curr == ')': right_counter += 1
        if curr == '(': left_counter += 1
    return left_counter == right_counter


# above method fails )( because it returns true order matters for this problem, so
# the next method addresses this

print(f'Expected output: True, actual output: {attempt_two('(())')}')
print(f'Expected output: True, actual output: {attempt_two('()()')}')
print(f'Expected output: False, actual output: {attempt_two('(()))')}')
print(f'Expected output: False, actual output: {attempt_two('((())')}')


def attempt_three(text):
    if len(text) == 0: return True
    left_counter = 0
    for i, curr in enumerate(text):
        if curr == '(':
            left_counter += 1
        elif curr == ')' and left_counter == 0:
            return False
        else:
            left_counter -= 1
    return left_counter == 0


print(f'Expected output: True, actual output: {attempt_three('(())')}')
print(f'Expected output: True, actual output: {attempt_three('()()')}')
print(f'Expected output: False, actual output: {attempt_three('(()))')}')
print(f'Expected output: False, actual output: {attempt_three('((())')}')
print(f'Expected output: False, actual output: {attempt_three(')(')}')


def brackets_recursive(index, text, left_counter):
    if index == len(text): return left_counter == 0
    if text[index] == '(':
        return brackets_recursive(index + 1, text, left_counter + 1)
    if text[index] == ')':
        if left_counter == 0:
            return False
        return brackets_recursive(index + 1, text, left_counter - 1)
    return brackets_recursive(index + 1, text, left_counter)


print(f'Expected output: True, actual output: {brackets_recursive(0, '(())', 0)}')
print(f'Expected output: True, actual output: {brackets_recursive(0, '()()', 0)}')
print(f'Expected output: False, actual output: {brackets_recursive(0, '(()))', 0)}')
print(f'Expected output: False, actual output: {brackets_recursive(0, '((())', 0)}')
print(f'Expected output: False, actual output: {brackets_recursive(0, ')(', 0)}')


def my_method(text):
    array = []
    str_counter = 0
    for row in range(3):
        current_row = []
        for col in range(3):
            if str_counter < len(text):
                current_row.append(text[str_counter])
                str_counter += 1
            else:
                current_row.append(None)
        array.append(current_row)
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print()
    return array


my_method('abcdefghi')
