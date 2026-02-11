def fractal_generator(n):
    if n < 0.125: return
    fractal_generator(n / 2)
    if n == 1:
        print("----")
    elif n == 0.5:
        print("---")
    elif n == 0.25:
        print("--")
    elif n == 0.125:
        print("-")
    fractal_generator(n / 2)

fractal_generator(1)


# print(fractal_generator(3))
def myMethod(n):
    for i in range(n):
        fractal_generator(i)


myMethod(4)
