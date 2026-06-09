from idlelib.debugger_r import restart_subprocess_debugger

import pytest


def all_combinations_with_value(base_values, desired_values):
    all_combinations = find_all_combinations(base_values)
    return find_by_value(all_combinations, desired_values)


def find_by_value(all_combinations, desired_value):
    return {key for key, value in all_combinations.items() if value == desired_value}


def find_all_combinations(digits):
    # recursive termination
    if len(digits) == 0:
        return {}
    if len(digits) == 1:
        last_digit = digits[0]
        return {last_digit: last_digit}
    # recursive descent
    left = digits[0]
    right = digits[1:]
    results = find_all_combinations(right)
    # create all combinations
    solutions = {}
    for expression, value in results.items():
        right_expr = str(expression)
        solutions[str(left) + "+" + right_expr] = eval(str(left) + "+" + right_expr)
        solutions[str(left) + "-" + right_expr] = eval(str(left) + "-" + right_expr)
        solutions[str(left) + right_expr] = eval(str(left) + right_expr)
    return solutions


@pytest.mark.parametrize("digits, expected", [([1, 2, 3],
                                               {"12-3": 9, "123": 123, "1+2+3": 6, "1+2-3": 0, "1-2+3": 2,
                                                "1-23": -22, "1-2-3": -4, "1+23": 24, "12+3": 15})])
def test_all_combinations(digits, expected):
    result = find_all_combinations(digits)
    assert result == expected
