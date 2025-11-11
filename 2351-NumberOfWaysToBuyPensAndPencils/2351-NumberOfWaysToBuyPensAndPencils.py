# Last updated: 11/10/2025, 8:01:20 PM
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        a = []
        res = 0
        for i in range(0, total+1):
            x = i % cost1 == 0
            if i - cost2 >= 0:
                x += a[i-cost2]
            a.append(x)
            res += x
        return res