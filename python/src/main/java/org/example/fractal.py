def fractal_generator(n):
    if n < 1: return
    if n == 1:
        print("-")
    else:
        fractal_generator(n - 1)
        print("=" * n)
        fractal_generator(n - 1)


print(fractal_generator(4))

