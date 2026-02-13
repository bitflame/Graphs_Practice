# ignores anything other than chars and numbers
def my_method(text):
    result = ''
    for i in text:
        if not (i.isalpha() or i.isdigit()):
            continue
        else:
            result += i
    return result


text = 'Was it a car or a cat I saw?'
text.join(" ")
print(my_method(text))
