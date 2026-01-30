class IndexOfFirst:
    def segSeg(self, haystack: str, needle: str) -> int:
        M = len(needle)
        N = len(haystack)
        if M > N: return -1
        R = 256
        right = [-1] * R
        for j, char in enumerate(needle):
            right[ord(char)] = j
        i = 0
        while i <= N - M:
            skip = 0
            for j in range(M - 1, -1, -1):
                if i + j < N and needle[j] != haystack[i + j]:
                    skip = j - right[ord(haystack[i + j])]
                    if skip < 1: skip = 1
                    break
                elif i + j > N:
                    return -1
            if i+j < N and skip == 0: return i
            i += max(skip,1)
        return -1


iof = IndexOfFirst()
haystack = "FINDINAHAYSTACKNEEDLEINA"
needle = "NEEDLE"
print(f'Test 1 - expected output: 15, actual: {iof.segSeg(haystack, needle)}')
haystack = "sadbustedsad"
needle = "sad"
print(f'Test 2 - expected output: 0, actual: {iof.segSeg(haystack, needle)}')
haystack = "leetcode"
needle = "leeto"
print(f'Test 3 - expected output: -1, actual: {iof.segSeg(haystack, needle)}')
haystack = "mississippi"
needle = "issip"
print(f'Test 4 - expected output: 4, actual: {iof.segSeg(haystack, needle)}')
haystack = "aaa"
needle = "aaaa"
print(f'Test 5 - expected output: -1, actual: {iof.segSeg(haystack, needle)}')
haystack = "mississippi"
needle = "a"
print(f'Test 6 - expected output: -1, actual: {iof.segSeg(haystack, needle)}')
haystack = "mississippi"
needle = "sippia"
print(f'Test 7 - expected output: -1, actual: {iof.segSeg(haystack, needle)}')
