import math

def print_pascal(n):
    print("Pascal's Triangle (with replacement):")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(cal_pascal(i, j), end=' ')
        print()
    print()


def print_all(n):
    print("Your print_all() output:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(cal_pascal(i, j), end=' ')
        print()
    print()


def cal_pascal(row, col):
    if row == 1: return 1
    if col == 1 or col == row: return 1
    return cal_pascal(row - 1, col - 1) + cal_pascal(row - 1, col)


def combination(n, k):
    """Calculate C(n, k) = n! / (k!(n-k)!)"""
    if k > n:
        return 0  # Can't choose more items than you have
    if k == 0 or k == n:
        return 1
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def print_combinations_grid(max_n):
    """Print all C(n, k) values in a grid format"""
    print("All C(n, k) combinations (without replacement):")
    print("Rows = n (total items), Columns = k (items chosen)")
    print()

    # Print header
    print("n\\k", end="  ")
    for k in range(max_n + 1):
        print(f"{k:4}", end=" ")
    print()
    print("-" * (6 * (max_n + 2)))

    # Print each row
    for n in range(max_n + 1):
        print(f"{n:2} ", end="  ")
        for k in range(max_n + 1):
            print(f"{combination(n, k):4}", end=" ")
        print()
    print()


# Run all demonstrations
print_pascal(5)
print_all(5)
print_combinations_grid(8)

print("\nKey observations:")
print("1. Pascal's triangle: Each row i has i entries (triangular shape)")
print("2. print_all(): Tries to print n entries per row, but cal_pascal() wasn't designed for this")
print("3. C(n,k) grid: Shows ALL combinations including when k > n (which = 0)")
print("4. Pascal's triangle is the DIAGONAL band where n >= k in the C(n,k) grid!")