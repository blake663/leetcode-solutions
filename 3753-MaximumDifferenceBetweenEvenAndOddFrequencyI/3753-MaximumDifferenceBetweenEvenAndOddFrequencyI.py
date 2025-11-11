# Last updated: 11/10/2025, 8:00:13 PM
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = 0
        min_even = math.inf
        for cnt in freq.values():
            if cnt & 1:
                max_odd = max(max_odd, cnt)
            else:
                min_even = min(min_even, cnt)
        return max_odd - min_even
