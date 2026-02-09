def print_pascal(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(cal_pascal(i, j), end=' ')
        print()


def print_all(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(cal_pascal(i, j), end=' ')
        print()


def cal_pascal(row, col):
    if row == 1: return 1
    if col == 1 or col == row: return 1
    return cal_pascal(row - 1, col - 1) + cal_pascal(row - 1, col)


print_pascal(5)
print_all(5)
