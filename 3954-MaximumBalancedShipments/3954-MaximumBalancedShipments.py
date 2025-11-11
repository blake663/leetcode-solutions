# Last updated: 11/10/2025, 7:59:34 PM
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        i = 1
        cnt = 0
        while i < n:
            if weight[i-1] > weight[i]:
                cnt += 1
                i += 2
            else:
                i += 1
        return cnt