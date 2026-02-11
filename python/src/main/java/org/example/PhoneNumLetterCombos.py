class Solution:
    def letter_combinations(self, digits: str) -> str:
        if len(digits) == 1: return digits
        combinations = ''
        for i, ch in enumerate(digits):
            permutations = self.letter_combinations(digits[:i] + digits[i+1:])
            for permutation in permutations:
                pass
        return combinations
digits = '23'
s = Solution()
print(s.letter_combinations(digits))