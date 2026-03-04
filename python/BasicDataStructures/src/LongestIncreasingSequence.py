import sys


def find_sequencee(values):
    longest_subsequence = []
    current_subsequence = []

    last_value = sys.maxsize
    for current_value in values:
        if current_value > last_value:
            last_value = current_value
            current_subsequence.append(current_value)
        else:
            if len(current_subsequence)> len(longest_subsequence):
                longest_subsequence = current_subsequence
            current_subsequence = []
            current_subsequence.append(current_value)
            last_value = current_value
    # to make sure the last subsequence is considered
    if len(current_subsequence) >= len(longest_subsequence):
        longest_subsequence = current_subsequence
    return longest_subsequence

values = [7,2,7,1,2,5,7,1]
print(find_sequencee(values))
values = [7,2,7,1,2,3,8,1,2,3,4,5]
print(find_sequencee(values))

# because we add the current_value to current_subsequence every time regardless of it being larger or smaller than the
# previous value we can do the following optimization
def optimized(values):
    longest_subsequence = []
    current_subsequence = []
    last_value = sys.maxsize
    for current_value in values:
        if current_value < last_value:
            if len(current_subsequence) >= len(longest_subsequence):
                longest_subsequence = current_subsequence
            current_subsequence = []
        last_value = current_value
        current_subsequence.append(current_value)
# you can use pointers into the same list instead of creating new lists
def yet_another_method(values):
    if len(values)==0:
        return values
    longest = (0,0)
    start_current = 0
    end_current = 0
    for end_current in range(1, len(values)):
        # flank change
        if values[end_current] < values[end_current-1]:
            if end_current - start_current > len(longest):
                longest = (start_current, end_current)
            start_current == end_current
        if end_current - start_current > len(longest):
            longest = (start_current, end_current)
    return values[longest[0]:longest[1]]
