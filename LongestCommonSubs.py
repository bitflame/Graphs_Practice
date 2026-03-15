def lcs(str1, str2):
    return lcs_helper(str1, str2, len(str1) - 1, len(str2) - 1)


def lcs_helper(str1, str2, pos1, pos2):
    if pos1 < 0 or pos2 < 0:
        return ""
    if str1[pos1] == str2[pos2]:
        return lcs_helper(str1, str2, pos1 - 1, pos2 - 1)
    else:
        lcs1 = lcs_helper(str1, str2, pos1, pos2 - 1)
        lcs2 = lcs_helper(str2, str2, pos1 - 1, pos2)
    return lcs1 if len(lcs1) > len(lcs2) else lcs2


def lcs_front(str1, str2):
    return lcs_front_helper(str1, str2, 0, 0)


def lcs_front_helper(str1, str2, pos1, pos2):
    if pos1 >= len(str1) or pos2 >= len(str2):
        return ""
    if str1[pos1] == str2[pos2]:
        return str1[pos1] + lcs_front_helper(str1, str2, pos1 + 1, pos2 + 1)
    else:
        lcs1 = lcs_front_helper(str1, str2, pos1, pos2 + 1)
        lcs2 = lcs_front_helper(str1, str2, pos1 + 1, pos2)
    return lcs1 if len(lcs1) > len(lcs2) else lcs2
