from enum import Enum
from random import randrange


class Direction(Enum):
    N = (0, -1)
    NE = (1, -1)
    E = (1, 0)
    SE = (1, 1)
    S = (0, 1)
    SW = (-1, 1)
    W = (-1, 0)
    NW = (-1, -1)

    def to_dx_dy(self):
        return self.value

    @classmethod
    def provide_random_direction(cls):
        random_index = randrange(len(list(Direction)))
        return list(Direction)[random_index]