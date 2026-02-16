def print_box(width, height, fill_char):
    x = 0
    for y in range(height):
        if x==0:
            if y==0:
                print('+', end=0)
            if y==height-1:
                print('+')
            else:
                print()
        if x == width-1:
            if y==0:
                print('+', end=0)
            if y==height-1:
                print('+')
        if (x == 0 and y == 0) or (x == 0 and y == height - 1) or (x == width - 1 and y == 0) or (
                x == width - 1 and y == height - 1):
            print('+')
            x += 1
        elif (x > 0 and x < width - 1 and y > 0) or (x > 0 and x < width - 1 and y < height - 1):
            print('|', end='')
            print('-' * width, end='')
            print('|')
            x += 1
        else:
            print('|', end='')
            print(fill_char * width, end='')
            print('|')
            x += 1

# need to use a nested loop
print_box(8, 9, '*')
print_box(8, 9, '@')
