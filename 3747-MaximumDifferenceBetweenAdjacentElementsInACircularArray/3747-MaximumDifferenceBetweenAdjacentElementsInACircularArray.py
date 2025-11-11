# Last updated: 11/10/2025, 8:00:19 PM
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = abs(nums[0] - nums[-1])

        for i in range(1, len(nums)):
            res = max(res, abs(nums[i-1] - nums[i]))
        
        return res