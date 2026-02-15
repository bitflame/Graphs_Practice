# 4.2.11
import pytest


def to_morse_code(text):
    morse_code = {'.': 'E', '---': 'O', '...': 'S', '-': 'T', '.--': 'W'}
    result = []
    for j in text.split('   '):
        for i, tone in enumerate(j.split(" ")):
            result.append(morse_code[tone])
        result.append('\n')
    return " ".join(result)


sos_text = '... --- ...'
print(f'{to_morse_code(sos_text)}')
tweet_text = '- .-- . . -'
print(f'{to_morse_code(tweet_text)}')
west_text = '.-- . ... -'
print(f'{to_morse_code(west_text)}')
sentence_text = '... --- ...   - .-- . . -   .-- . ... -'
print(f'{to_morse_code(sentence_text)}')


# 4.2.12 Patter Checker
def matches_pattern(pattern, text):
    # prepare
    values = text.split(" ")
    if len(values) != len(pattern) or (len(values) == 1 and not values[0]):
        return False
    placeholder_to_value_map = {}
    # process all characters
    for i, pattern_char in enumerate(pattern):
        value = values[i]

        # add, if not already there
        if pattern_char not in placeholder_to_value_map:
            placeholder_to_value_map[pattern_char] = value

        # does stored value match current string?
        assigned_value = placeholder_to_value_map[(pattern_char)]
        if not assigned_value == value:
            return False
    return True


@pytest.mark.parametrize("pattern, input, expected",
                         [("x", "", False),
                          ("", "x", False)])
def test_matches_pattern_special_cases(pattern, input, expected):
    assert matches_pattern(pattern, input) == expected


@pytest.mark.parametrize("pattern, input, expected",
                         [("xyyx", "tim mike mike tim", True),
                          ("xyyx", "time mike tom tim", False),
                          ("xyxx", "tim mike mike tim", False),
                          ("xxxx", "tim tim tim tim", True)])
def test_matches_pattern(pattern, input, expected):
    assert matches_pattern(pattern, input) == expected
