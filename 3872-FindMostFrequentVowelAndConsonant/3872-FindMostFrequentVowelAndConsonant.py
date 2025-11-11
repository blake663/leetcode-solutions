# Last updated: 11/10/2025, 8:00:01 PM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        vow, con = Counter({'a': 0}), Counter({'b': 0})

        for c in s:
            if c in vowels:
                vow[c] += 1
            else:
                con[c] += 1
        
        return max(vow.values()) + max(con.values())