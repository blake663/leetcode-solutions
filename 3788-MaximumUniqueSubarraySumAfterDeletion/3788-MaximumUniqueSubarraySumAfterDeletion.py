# Last updated: 11/10/2025, 8:00:09 PM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if not any(num >= 0 for num in nums):
            return max(nums)
        seen = set()
        total = 0
        for num in nums:
            if num > 0 and num not in seen:
                total += num
                seen.add(num)
        return total