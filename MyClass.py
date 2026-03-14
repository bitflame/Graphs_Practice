def hanoi(n, source, auxiliary, destination):
    if n <= 1:
        print(source, '->', destination)
    else:
        hanoi(n - 1, source, destination, auxiliary)
        print(source,'->', destination)
        hanoi(n - 1, auxiliary, source, destination)

src = 'A'
aux = 'B'
dest = 'C'
hanoi(3, src, aux, dest)
