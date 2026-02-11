def fractal_gen(n):
    if n < 1:
        return
    if n == 1:
        print(f'-')
    else:
        fractal_gen(n - 1)
        print("=" * n)
        fractal_gen(n - 1)
fractal_gen(3)