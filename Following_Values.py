import pytest


def generate_following_values_for_predefined(predefined_values, current_value, sequence_length):
    result = []
    current_pos = predefined_values.index(current_value)
    while sequence_length > 0:
        result.append(current_value)
        current_value, current_pos = next_cyclic(predefined_values, current_pos)
        sequence_length -= 1
    return result


def next_cyclic(values, current_pos):
    next_pos = (current_pos + 1) % len(values)
    return values[next_pos], next_pos


def predefined_values():
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


@pytest.mark.parametrize("predefined_values, current_value, "
                         "sequence_length, expected",
                         [(predefined_values(), "Monday", 3, ["Monday", "Tuesday", "Wednesday"]),
                          (predefined_values(), "Friday", 8,
                           ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])])
def test_generate_following_values_for_predefined(predefined_values, current_value, sequence_length, expected):
    result = generate_following_values_for_predefined(predefined_values, current_value, sequence_length)
    assert result == expected
