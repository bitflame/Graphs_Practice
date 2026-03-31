from enum import Enum, auto


def test_index():
    # arrange
    name = "Peter"
    # act
    pos = name.index("t")
    expected = 2
    # assert
    assert pos == expected

######################################################3
class Gender(Enum):
        MALE = auto()
        FEMALE = auto()

