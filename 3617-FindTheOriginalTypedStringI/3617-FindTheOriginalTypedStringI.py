# Last updated: 11/10/2025, 8:00:29 PM
class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1 + len([1 for x, y in zip(word, word[1:]) if x == y])
        return res