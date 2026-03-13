from TowersOfHanoi import move_tower
from python.BasicDataStructures.src.MyStack import MyStack


class Tower:
    def __init__(self, name):
        self.name = name
        self.values = MyStack()

    def __str__(self):
        return "Tower [" + self.name + "]"

    def push(self, item):
        self.values.push(item)

    def pop(self):
        return self.values.pop()

    def print_tower(self, max_height):
        height = self.values.size() - 1
        visual = self.draw_top(max_height, height)
        visual += self.draw_slices(max_height, height)
        visual += self.draw_bottom(max_height)
        return visual

    def draw_top(self, max_height, height):
        visual = [" " * max_height + self.name + " " * max_height]
        for i in range(max_height - height - 1, 0, -1):
            visual.append(" " * max_height + "|" + " " * max_height)
        return visual

    def draw_slices(self, max_height, height):
        visual = []
        for i in range(height, -1, -1):
            value = self.values.get_at(i)  # ? __values or values?
            padding = max_height - value
            visual.append(" " * padding + "#" * value + "|" + "#" * value + " " * padding)
        return visual

    def draw_bottom(self, height):
        return ["-" * (height * 2 + 1)]


def print_towers(max_height, source, helper, destination):
    tower1 = source.print_tower(max_height)
    tower2 = helper.print_tower(max_height)
    tower3 = destination.print_tower(max_height)
    for (a, b, c) in zip(tower1, tower2, tower3):
        print(a + "  " + b + "  " + c)


def solve_tower_of_hanoi_v2(n):
    print("Tower Of Hanoi", n)
    source = Tower("A")
    helper = Tower("B")
    destination = Tower("C")
    # attention: rever order: largest slice first
    for i in range(n, 0, -1):
        source.push(i)
    action = lambda: print_towers(n + 1, source, helper, destination)
    action()
    move_tower_v2(n, source, helper, destination, action)


def move_tower_v2(n, source, helper, destination, action):
    if n == 1:
        elem_to_move = source.pop()
        destination.push(elem_to_move)
        print("Moving slice: ", elem_to_move, ":", source, "->", destination)
        action()
    else:
        move_tower_v2(n - 1, source, destination, helper, action)
        move_tower_v2(1, source, helper, destination, action)
        move_tower_v2(n - 1, helper, source, destination, action)


solve_tower_of_hanoi_v2(3)
