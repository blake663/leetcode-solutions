# Last updated: 11/10/2025, 8:00:33 PM
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        res = n * (n+1) // 2

        freq = Counter()
        l = 0
        for r, c in enumerate(s):
            freq[c] += 1
            while freq[c] == k:
                freq[s[l]] -= 1
                l += 1
            res -= r - l + 1
        return res