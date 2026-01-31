
class RabinKarp:
    def strStr(self, haystack: str, needle: str) -> int:
        Q = 2 ** 61 - 1
        RM = 1
        M = len(needle)
        N = len(haystack)
        if M > N: return -1
        R = 256
        for _ in range(M-1):
            RM = R * RM % Q
        patHash = self.hash(needle, Q, M)
        txtHash = self.hash(haystack[:M], Q, M)
        if patHash == txtHash: return 0
        for i in range(M, N, 1):
            txtHash = (txtHash + Q - RM * ord(haystack[i-M]) % Q) % Q
            txtHash = (txtHash * R + ord(haystack[i])) % Q
            if patHash == txtHash: return i - M + 1
        return -1

    def hash(self, needle: str, Q: int, end:int) -> int:
        h = 0
        R = 256
        for i in range(end):
            h = (R * h + ord(needle[i]))%Q
        return h


rk = RabinKarp()
haystack = "NEEDLE"
needle = "NEEDLE"
print(f'Test 1 - expected output: 0, actual: {rk.strStr(haystack, needle)}')
haystack = "FINDINAHAYSTACKNEEDLEINA"
needle = "NEEDLE"
print(f'Test 2 - expected output: 15, actual: {rk.strStr(haystack, needle)}')
haystack = "sadbustedsad"
needle = "sad"
print(f'Test 3 - expected output: 0, actual: {rk.strStr(haystack, needle)}')
haystack = "leetcode"
needle = "leeto"
print(f'Test 4 - expected output: -1, actual: {rk.strStr(haystack, needle)}')
haystack = "mississippi"
needle = "issip"
print(f'Test 5 - expected output: 4, actual: {rk.strStr(haystack, needle)}')
haystack = "aaa"
needle = "aaaa"
print(f'Test 6 - expected output: -1, actual: {rk.strStr(haystack, needle)}')
haystack = "mississippi"
needle = "a"
print(f'Test 7 - expected output: -1, actual: {rk.strStr(haystack, needle)}')
haystack = "mississippi"
needle = "sippia"
print(f'Test 8 - expected output: -1, actual: {rk.strStr(haystack, needle)}')
