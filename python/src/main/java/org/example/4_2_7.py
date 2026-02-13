def change_to_Title(text):
    result = ''
    for word in text.split():
        result += word[0].upper() + word[1:] + ' '
    return result


print(f'{change_to_Title('this is a very special title')}')
print(f'{change_to_Title('effective java is great')}')


# lets use a list for collecting the results
def new_way(text):
    words = []
    for word in text.split():
        if word:
            words.append(word[0].upper() + word[1:])
    return "".join(words)


def another_way(text):
    return " ".join(w[:1].upper() + w[1:] for w in text.split())


print(f'last method: {another_way('effective java is great')}')


# this one returns a list of the words rather than a string
def four_seven_b(text):
    words = []
    for word in text.split():
        if word:
            words.append(word[0].upper() + word[1:])
    return words


def four_seven_c(text, ignor):
    ignor_list = set(ignor)
    # was not sure if I should use a set or a list above
    words = []
    for word in text:
        if word.lower() not in ignor_list:
            word = word[0].upper() + word[1:]
        words.append(word)
    return words


inp = ['this', 'is', 'a', 'title']
exceptions = ['is', 'a']
print(
    f'Test 1 - Special Treatment expected output: [\'This\',\'is\', \'a\',\'Title\'] actual output: {four_seven_c(inp, exceptions)}')
