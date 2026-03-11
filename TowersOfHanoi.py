def move_tower(n, source, helper, destination):
    if n == 1:
        print(source + "->" + destination)
    else:
        # move all the disks except the last one to the aux
        # so destination and helper swap places
        move_tower(n - 1, source, destination, helper)
        # move the last disk / the largest disk to the destination
        print(source + "->" + destination)
        # move_tower(1, source, helper, destination)
        # move the rest of the disks to the destination
        move_tower(n - 1, helper, source, destination)


def solve_tower_of_hanoi(n):
    print("Tower of Hanoi", n)
    move_tower(n, 'A', 'B', 'C')


solve_tower_of_hanoi(3)
