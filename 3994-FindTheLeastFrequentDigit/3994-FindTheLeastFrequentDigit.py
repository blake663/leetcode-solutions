# Last updated: 11/10/2025, 7:59:34 PM
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = [0] * 10
        for c in str(n):
            freq[int(c)] += 1

        cnt, res = 100, 0
        for val, frq in enumerate(freq):
            if frq and frq < cnt:
                cnt = frq
                res = val

        return res