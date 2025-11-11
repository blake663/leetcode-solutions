# Last updated: 11/10/2025, 8:00:12 PM
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        res = 0
        for i in range(len(nums)//3):
            res += nums[n-2-(i*2)]

        return res