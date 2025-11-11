# Last updated: 11/10/2025, 7:59:47 PM
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = sum(int(c) for c in str(n))
        p = prod(int(c) for c in str(n))

        return n % (s + p) == 0