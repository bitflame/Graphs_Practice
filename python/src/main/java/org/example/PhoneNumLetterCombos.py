from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> str:
        if len(digits) == 1: return digits
        numbers = {1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wzyz', 0: ''}
        return ''.join(self.helper(digits, numbers, 0, []))

    def helper(self, digits: str, numbers, index, combinations) -> List:
        if index == len(digits): return combinations
        characters = numbers.get(int(digits[index]))
        if len(combinations) == 0:
            for character in characters:
                combinations.append(character)
        else:
            new_combos = []
            for character in characters:
                for i in range(len(combinations)):
                    segment = combinations[i] + character
                    new_combos.append(segment)
            combinations = new_combos
        combinations = self.helper(digits, numbers, index + 1, combinations)
        return combinations


digits = '23'
s = Solution()
print(s.letter_combinations(digits))

