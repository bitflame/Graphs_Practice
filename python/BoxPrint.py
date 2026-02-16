def print_box(width, height, fill_char):
    for h in range(height):
        if h == 0 or h == height - 1:
            print('|', end='')
            print('-' * width, end='')
            print('|')
        else:
            print('|', end='')
            print(fill_char * width, end='')
            print('|')


print_box(8, 9, '*')
print_box(8, 9, '@')