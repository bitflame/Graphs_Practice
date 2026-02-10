def fractal_generator(n):
    if n < 1: return
    if n == 1:
        print("-")
    else:
        fractal_generator(n - 1)
        print("=" * n)
        fractal_generator(n - 1)


print(fractal_generator(2))


def ruler(n):
    if n == 0: return n
    print('-' * n * 2 + f'{ruler(n - 1)}')


print('Calling ruler')
ruler(2)
