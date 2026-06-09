def all_combos(digits, desired_value):
    all_combos = helper_function(digits)
    return look_for_value(all_combos, desired_value)


def look_for_value(all_combos, desired_value):
    return {key for key, value in all_combos.items() if value == desired_value}


def helper_function(digits):
    if len(digits) == 0:
        return {}
    elif len(digits) == 1:
        last_digit = digits[0]
        return {last_digit: last_digit}
    else:
        l = digits[0]
        r = digits[1:]
        results = helper_function(r)
        solutions = {}
        # the key is l & r with one operator between them
        for expression, value in results.items():
            right_expression = str(expression)
            solutions[str(l) + "+" + right_expression] = eval(str(l) + "+" + right_expression)
            solutions[str(l) + "-" + right_expression] = eval(str(l) + "-" + right_expression)
            solutions[str(l) + right_expression] = eval(str(l) + right_expression)
    return solutions


my_digits = [1, 2, 3]
print(all_combos(my_digits, 123))
print(all_combos(my_digits, 9))
print(all_combos(my_digits, 6))
print(all_combos(my_digits, 0))
print(all_combos(my_digits, 2))
print(all_combos(my_digits, -22))
print(all_combos(my_digits, -4))
print(all_combos(my_digits, 24))
print(all_combos(my_digits, 15))


def all_combinations(values):
    return my_helper_function(values, 0, [], [])


def my_helper_function(values, index, path, result):
    if index == len(values):
        result.append(path[:])
        return result
    else:
        path.append(values[index])
        my_helper_function(values, index + 1, path, result)
        path.remove(values[index])
        my_helper_function(values, index + 1, path, result)
    return result


my_values = [1, 2, 3, 4]
print(all_combinations(my_values))
'''
Base Case
Choices
Constraints
Backtracking step 
def backtrack(params): 
     if base_case_condition: 
     results.append(copy_of_solution)
     return
     for choice in choices: 
          if violates_constraints:
                continue
          make_choice
          backtrac(updated_params)
          undo_choice
          
Problems solvable via backtracking
Permutations - Given a list of numbers return all possible permutations. 

'''
