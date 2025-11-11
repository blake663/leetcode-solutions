# Last updated: 11/10/2025, 8:00:41 PM
class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'

        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        if not any(c.lower() in vowels for c in word):
            return False
        if not any(c.isalpha() and c.lower() not in vowels for c in word):
            return False
        return True