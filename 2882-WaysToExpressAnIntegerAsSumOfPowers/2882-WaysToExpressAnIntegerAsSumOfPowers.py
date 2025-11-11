# Last updated: 11/10/2025, 8:00:50 PM
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        i_max = int(n**(1/x) + .001)

        count = [0] * (n+1)
        count[0] = 1

        for i in range(1, i_max+1):
            p = i**x
            for j in range(n - p, -1, -1):
                count[j+p] += count[j]
        
        return count[n] % (10**9 + 7)