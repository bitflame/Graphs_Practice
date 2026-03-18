def finder(variable_string):
    return helper(variable_string.lower(), 0, 0, [], [])


def helper(current_string, start, end, current_pal, results):
    if start < 0 or end > len(current_string) - 1:
        return results
    if current_string[start] == current_string[end]:
        current_pal.append(current_string[start])
        if end > start:
            current_pal.append(current_string[end])
        helper(current_string, start - 1, end + 1, current_pal, results)
    elif len(current_pal) > 1:
        results.append(current_pal)
        return results
    results = helper(current_string, start + 1, end + 1, [], results)
    return results


print(finder("BCDEDCB"))
print(finder("ABALOTTOLL"))
print(finder("racecar"))
