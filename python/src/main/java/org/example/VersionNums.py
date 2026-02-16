def compare_versions(version1, version2):
    v1_nums = version1.split(".")
    v2_nums = version2.split(".")
    pos = 0
    compare_result = "="
    while pos < len(v1_nums) and pos<(v2_nums) and compare_result == "=":
        current_v1 = int(v1_nums[pos])
        current_v2 = int(v2_nums[pos])
        compare_result = compare(current_v1, current_v2)
        pos +=1
    if compare_result == "=":
        return compare(len(v1_nums), len(v2_nums))
    return compare_result
def compare(val1, val2):
    if val1 < val2: return "<"
    if val1 > val2: return ">"
    return "="