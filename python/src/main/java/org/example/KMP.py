def kmp(pat):
    m = len(pat)
    R = 256
    dfa = [[0] * m for _ in range(R)]
    dfa[ord(pat[0])][0] = 1
    x = 0
    for j in range(1, m):
        for c in range(R):
            dfa[c][j]=dfa[c][x]
        dfa[ord(pat[j])][j]=j+1
        x = dfa[ord(pat[j])][x]
    return dfa

def search(text, pat):
    M = len(pat)
    j = 0
    dfa = kmp(pat)
    for i, ch in enumerate(text):
        j = dfa[ord(ch)][j]
        if j == M:
            # sedgewick does not add 1 below, but AI does
            return i - M + 1
    return -1

def kmp_rotation_contains(str1, str2):
    if len(str2)==0: return True
    if len(str1)==0: return False
    if len(str2)>len(str1): return False
    return search(str1+str1,str2)!=-1
