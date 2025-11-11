# Last updated: 11/10/2025, 8:00:59 PM
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        res = []
        powers = []

        p = 0
        while 1<<p <= n:
            if 1<<p & n:
                powers.append(p)
            p += 1

        # prefix sum array
        pref = [0] * (len(powers)+1)
        for p in range(len(powers)):
            pref[p+1] = pref[p] + powers[p]

        for l, r in queries:
            res.append(pow(2, pref[r+1] - pref[l], mod=MOD))
        
        return res