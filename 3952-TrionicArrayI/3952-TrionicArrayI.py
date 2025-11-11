# Last updated: 11/10/2025, 7:59:35 PM
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1
        if i == n or nums[i-1] >= nums[i]: return False
        while i < n and nums[i-1] < nums[i]:
            i = i+1
        if i == n or nums[i-1] <= nums[i]: return False
        while i < n and nums[i-1] > nums[i]:
            i = i+1
        if i == n or nums[i-1] >= nums[i]: return False
        while i < n and nums[i-1] < nums[i]:
            i = i+1
        return i == n