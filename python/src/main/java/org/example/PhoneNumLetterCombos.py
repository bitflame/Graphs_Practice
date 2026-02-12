class Solution:
    def letter_combinations(self, digits: str) -> str:
        if len(digits) == 1: return digits
        numbers = {1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9:'wzyz',0:''}
        print(numbers.get(3))


    def helper(self, digits: str, numbers) -> str:
        combinations = ''
        for i, ch in enumerate(digits):
            permutations = self.helper(digits[:i] + digits[i + 1:], numbers)
            for permutation in permutations:
                pass
        return combinations

digits = '23'
s = Solution()
print(s.letter_combinations(digits))
