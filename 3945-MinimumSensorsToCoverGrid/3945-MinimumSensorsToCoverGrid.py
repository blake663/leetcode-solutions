# Last updated: 11/10/2025, 7:59:37 PM
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        span = 2*k + 1
        return math.ceil(n/span) * math.ceil(m/span)