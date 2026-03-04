from MyStack import MyStack


def well_formed(some_string):
    chars = {'(': ')', '[': ']', '{': '}'}
    stack = MyStack()
    for some_char in some_string:
        if some_char in chars.keys():
            stack.push(some_char)
        elif not stack.is_empty() and chars[stack.peek()] == some_char:
            stack.pop()
        else:
            return False
    return stack.is_empty()


some_string = '(())'  # True
print(well_formed(some_string))
some_string = '({[]})'  # True
print(well_formed(some_string))
some_string = '((())'  # False
print(well_formed(some_string))
some_string = '((a)'  # False
print(well_formed(some_string))
some_string = '((])'  # False
print(well_formed(some_string))
some_string = 'a'  # False
print(well_formed(some_string))
some_string = ')'  # False
print(well_formed(some_string))


# different way
def is_openning_parenthesis(ch):
    return ch == '(' or ch == '[' or ch == '{'


def is_closing_parenthesis(ch):
    return ch in [')', ']', '}']


def is_matching_parenthesis_pair(opening, closing):
    return (opening == '(' and closing == ')') or (opening == '[' and closing == ']') or (
                opening == '{' and closing == '}')


def check_parenthesis(braces_input):
    # odd length cannot be a well-formed bracing
    if len(braces_input) % 2 != 0: return False
    opening_parentheses = MyStack()
    for char in braces_input:
        if is_openning_parenthesis(char):
            opening_parentheses.push(char)
        elif is_closing_parenthesis(char):
            if opening_parentheses.is_empty():
                # closing before opening brace
                return False
            last_opening_parens = opening_parentheses.pop()
            if not is_matching_parenthesis_pair(last_opening_parens, char):
                return False
        else:
            # invalid char
            return False
    return opening_parentheses.is_empty()
