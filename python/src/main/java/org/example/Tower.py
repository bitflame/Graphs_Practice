def print_tower(height):
    draw_top(height)
    draw_slices(height)
    draw_bottom(height)


def draw_top(height):
    print(" " * (height + 1) + "|")


def draw_bottom(height):
    print("-" * ((height + 1) * 2 + 1))


def draw_slices(height):
    for i in range(height - 1, -1, -1):
        value = height - i
        padding = i + 1
        print(" " * padding + "#" * value + "|" + "#" * value)


def draw_slices_rec(slice, height):
    if slice > 1:
        draw_slices_rec(slice - 1, height)
    print(" " * (height - slice + 1) + "#" * slice + "|" + "#" * slice)


def print_tower_rec(height):
    draw_top(height)
    draw_slices_rec(height, height)
    draw_bottom(height)


print_tower(4)
