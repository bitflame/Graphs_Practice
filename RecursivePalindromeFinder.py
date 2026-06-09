


def all_palindrom_parts(input):
    results = set()
    all_palindrome_parts_rec(input, 0, len(input)-1, results)
    return results
def all_palindrome_parts_rec(input, left, right, results):
    # recursive termination
    if left >= right:
        return
    #1) check if the whole string is a palindrome
    complete_is_palindrome = is_palindrome_rec_range(input, left, right)
    if complete_is_palindrome:
        new_candidate = input[left:right+1]
        results.add(new_candidate)
    for i in range(left+1, right):
        left_part_is_palindrome = is_palindrome_rec_range(input,i, right)
        if left_part_is_palindrome:
            new_candidate = input[i:right+1]
            results.add(new_candidate)
    for i in range(right-1, left, -1):
        right_part_is_palindrome = is_palindrome_rec_range(input, left, i)
        if right_part_is_palindrome:
            new_candidate = input[left: i+1]
            results.add(new_candidate)
    # recursive descent
    all_palindrome_parts_rec(input, left+1, right-1, results)

def is_palindrome_rec_range(input, left, right):
    if left >= right:
        return True
    if input[left]==input[right]:
        # recursive descent
        return is_palindrome_rec_range(input, left+1, right-1)
    return False

# the following optimized version calls itself for the shortened version from left and right, instead of reduing
# the input from both sides and having to iterate through shorter versions of each side repeatedly, so there are
# no loops in this one.
def all_palindrome_parts_rec_optimized(input):
    results = set()
    all_palindrom_parts_rec_optimized_(input, 0,len(input)-1, results)
    return results
def all_palindrom_parts_rec_optimized_(input, left, right, results):
    if left>= right:
        return
    if is_palindrome_rec_range(input, left, right):
        results.add(input[left:right+1])
    # recursive descent
    all_palindrom_parts_rec_optimized_(input, left+1, right, results)
    all_palindrom_parts_rec_optimized_(input, left, right-1, results)

# print(all_palindrom_parts("BCDEDCB"))
# print(all_palindrom_parts("ABALOTTOLL"))
# print(all_palindrom_parts("racecar"))

# print(all_palindrome_parts_rec_optimized("BCDEDCB"))
# print(all_palindrome_parts_rec_optimized("ABALOTTOLL"))
# print(all_palindrome_parts_rec_optimized("racecar"))

# yet a more readable version...
def all_pal_parts_rec_opt(input):
    results = set()
    all_palindrom_parts_v3(input, results)
    return results
def all_palindrom_parts_v3(input, results):
    if len(input) < 2:
        return
    if is_palindrome_rec_range(input, 0, len(input)-1):
        results.add(input)
    all_palindrom_parts_v3(input[1:], results)
    all_palindrom_parts_v3(input[0:len(input)-1],results)

print(all_pal_parts_rec_opt("BCDEDCB"))
print(all_pal_parts_rec_opt("ABALOTTOLL"))
print(all_pal_parts_rec_opt("racecar"))