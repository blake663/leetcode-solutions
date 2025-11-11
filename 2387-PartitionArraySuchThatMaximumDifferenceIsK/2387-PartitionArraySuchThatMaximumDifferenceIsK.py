# Last updated: 11/10/2025, 8:01:14 PM
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        mn = nums[0]
        for num in nums:
            if num > mn + k:
                count += 1
                mn = num
        
        return count