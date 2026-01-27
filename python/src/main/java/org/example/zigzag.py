class zigzag:
    # code below from NeetCode
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ""
        for r in range(numRows):
            increment = (numRows - 1) * 2
            for i in range(r, len(s), increment):
                res += s[i]
                if r != 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res
# code below from algomaps.io
    def methodTwo(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        i = 0
        d = 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d

        ret = ''
        for i in range(numRows):
            ret += ''.join(rows[i])

        return ret


s = "PAYPALISHIRING"
z = zigzag()
print(f'Test 1 - input: PAYPALISHIRING and 3 rows. expected output: PAHNAPLSIIGYIR. Actual output: {z.convert(s, 3)}')

print(f'Test 2 - input: PAYPALISHIRING and 4 rows. expected output: PINALSIGYAHRPI. Actual output: {z.convert(s, 4)}')
