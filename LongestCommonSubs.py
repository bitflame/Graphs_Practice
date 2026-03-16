import time


def lcs(str1, str2):
    return lcs_helper(str1, str2, len(str1) - 1, len(str2) - 1)


def lcs_helper(str1, str2, pos1, pos2):
    if pos1 < 0 or pos2 < 0:
        return ""
    if str1[pos1] == str2[pos2]:
        return lcs_helper(str1, str2, pos1 - 1, pos2 - 1) + str1[pos1]
    else:
        lcs1 = lcs_helper(str1, str2, pos1, pos2 - 1)
        lcs2 = lcs_helper(str1, str2, pos1 - 1, pos2)
    return lcs1 if len(lcs1) > len(lcs2) else lcs2


first_string = 'ABCE'
second_string = 'ZACEF'
# print(f'Test 1 - expected answer: ACE, actual answer:  {lcs(first_string, second_string)}')

'''@pytest.mark.parametrize("value1, value2, expected",
                         [("ABCE", "ZACED", "ACE"),
                          ("ABCXY", "XYACB", "AB"),
                          ("ABCMIXCHXAEL", "MICHAEL", "MICHAEL")])
def test_lcs(value1, value2, expected):
    result = lcs(value1, value2)
    assert result == expected'''


def lcs_optimized(str1, str2):
    values = [[None for _ in range(len(str2))] for _ in range(len(str1))]
    return lcs_with_memo(str1, str2, len(str1) - 1, len(str2) - 1, values)


def lcs_with_memo(str1, str2, pos1, pos2, values):
    if pos1 < 0 or pos2 < 0:
        return ""
    if values[pos1][pos2] is not None:
        return values[pos1][pos2]
    lcs = ""
    if str1[pos1] == str2[pos2]:
        lcs = lcs_with_memo(str1, str2, pos1 - 1, pos2 - 1, values) + str1[pos1]
    else:
        lcs1 = lcs_with_memo(str1, str2, pos1, pos2 - 1, values)
        lcs2 = lcs_with_memo(str1, str2, pos1 - 1, pos2, values)
        lcs = lcs1 if len(lcs1) > len(lcs2) else lcs2
    values[pos1][pos2] = lcs
    return lcs


def main():
    inputs_tuples = [["ABCMIXCHXAEL", "MICHAEL"],
                     ["sunday-Morning", "saturday-Night-party"],
                     ["sunday-morning-Wakeup", "saturday-Night"]]
    for inputs in inputs_tuples:
        start = time.process_time()
        result = lcs(inputs[0], inputs[1])
        end = time.process_time()

        print(inputs[0] + " -> " + inputs[1] + " lcs:" + result)
        print("lcs() took %.2f ms" % ((end - start) * 1000))
    for inputs in inputs_tuples:
        start = time.process_time()
        result = lcs_optimized(inputs[0], inputs[1])
        end = time.process_time()
        print(inputs[0] + " -> " + inputs[1] + " lcs_optimized:" + result)
        print("lcs() took %.2f ms" % ((end - start) * 1000))


def lcs_from_start(str1, str2):
    values = [[None for _ in range(len(str2))] for _ in range(len(str1))]
    return lcs_from_start_helper(str1, str2, 0, 0, values)


def lcs_from_start_helper(str1, str2, pos1, pos2, values):
    if pos1 >= len(str1) or pos2 >= len(str2):
        return ""
    if values[pos1][pos2] is not None:
        return values[pos1][pos2]
    if str1[pos1] == str2[pos2]:
        return str1[pos1] + lcs_from_start_helper(str1, str2, pos1 + 1, pos2 + 1, values)
    else:
        lcs1 = lcs_from_start_helper(str1, str2, pos1, pos2 + 1, values)
        lcs2 = lcs_from_start_helper(str1, str2, pos1 + 1, pos2, values)
        result = lcs1 if len(lcs1) > len(lcs2) else lcs2
        values[pos1][pos2] = result
    return result


def main_two():
    # inputs_tuples = [["ABCMIXCHXAEL", "MICHAEL"],
    #                  ["sunday-Morning", "saturday-Night-party"],
    #                  ["sunday-morning-Wakeup", "saturday-Night"]]
    inputs_tuples = [["ABCE", "ZACEF"],
                     ["Micha", "Michael"],
                     ["ABCXY", "XYACB"],
                     ["ABCMIXCHXAEL", "MICHAEL"],
                     ["sunday-Morning", "saturday-Night-party"],
                     ["sunday-Morning-Wakeup", "saturday-Night"]]
    for i, inputs in enumerate(inputs_tuples):
        start = time.process_time()
        result = lcs_from_start(inputs[0], inputs[1])
        end = time.process_time()

        print(f"Test {1 + i} - " + inputs[0] + " -> " + inputs[1] + " lcs:" + result)
        print("lcs() took %.2f ms" % ((end - start) * 1000))


main_two()
