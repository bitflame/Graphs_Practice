def fractal_generator(index, n):
    if n < 0.125: return
    if n % 1 == 0:
        print(f"---- {index}")
    fractal_generator(index, n / 2)
    if n == 0.5:
        print("---")
    elif n == 0.25:
        print("--")
    elif n == 0.125:
        print("-")
    if n < 1:
        fractal_generator(index, n / 2)

# fractal_generator(1)


# print(fractal_generator(3))
def myMethod(n):
    for i in range(n):
        # print(f'---- {i}')
        fractal_generator(i, 1)


myMethod(4)
