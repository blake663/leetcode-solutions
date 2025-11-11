# Last updated: 11/10/2025, 8:00:31 PM
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = {v: 0 for v in vowels}
        total_count = 0
        n = len(word)
        def all_vowels_present(vowel_count):
            return all(vowel_count[v] > 0 for v in vowels)

        for start in range(n):
            consonant_count = 0
            vowel_count = {v: 0 for v in vowels}
            for end in range(start, n):
                char = word[end]

                if char in vowels:
                    vowel_count[char] += 1
                elif char.isalpha():
                    consonant_count += 1
                if all_vowels_present(vowel_count) and consonant_count == k:
                    total_count += 1

        return total_count