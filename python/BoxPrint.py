def print_box(width, height, fill_char):
    for row in range(height):
        for col in range(width):
            if row == 0:
                if col == 0:
                    print('+', end='')
                if col == width - 1:
                    print('+')
                else:
                    print('-', end='')
            elif row == height - 1:
                if col == 0:
                    print('+', end='')
                if col == width - 1:
                    print('+')
                else:
                    print('-', end='')
            else:
                if col == 0:
                    print('|', end='')
                if col == width - 1:
                    print('|')
                else:
                    print(fill_char, end='')


print('     another run           ')
print_box(8, 9, '*')
print('     another run           ')
print_box(8, 9, '@')
print('     another run           ')
print_box(8, 9, '$')
