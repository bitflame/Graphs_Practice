
strange_message = "a message containing only a message"

mid_chars = strange_message[10:20]
last_seven_chars = strange_message[-7:]
print("mid_chars: ", mid_chars, " / last_seven_chars: ", last_seven_chars)
first_char = strange_message[0]
print(first_char, "count:", strange_message.count(first_char))
print(last_seven_chars, "count: ", strange_message.count(last_seven_chars))
# search and continue searching
print("find message: ", strange_message.find("message"))
print("find next message: ", strange_message.find("message", 3))
print(last_seven_chars, "count: ", strange_message.find("message",3))
# replace (all)
print("replace by info: ", strange_message.replace("message","info") )
# to convert a string to a list of chars...
print(list("Text as a list of chars"))
message = 'python has several loop variants'
for i in range(len(message)):
    print(i, message[i], end=',')
print()
for i, current_char in enumerate(message):
    print(i, current_char, end=',')
print()
for current_char in message:
    print(current_char, end=',')
print()
text = ('this is a very special string')
print(text.capitalize())
print(text.title())
product = "Apple iMac"
price = 3699
# variants of the formatted output
print('The {} costs {}'.format(product, price))
print(f'The %s costs %d'% (product,price))