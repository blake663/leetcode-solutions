# Last updated: 11/10/2025, 8:01:03 PM
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        nearest = [0] * 30

        for i in range(n-1, -1, -1):
            for b in range(30):
                if nums[i] & 1<<b:
                    nearest[b] = i
            res[i] = max(max(nearest) - i + 1, 1)
        
        return res
