# Last updated: 11/10/2025, 8:00:48 PM
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        v_set = set(vowels)
        vowel_index = 0
        freq = Counter(c for c in s if c in v_set)

        res = []
        for c in s:
            if c in freq:
                while freq[vowels[vowel_index]] == 0:
                    vowel_index += 1
                res.append(vowels[vowel_index])
                freq[vowels[vowel_index]] -= 1
            else:
                res.append(c)
        
        return ''.join(res)