# Last updated: 11/10/2025, 8:00:54 PM
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0

        nums.sort()

        l, r = 0, max(nums) - min(nums)

        while l < r: 
            mid = (l + r) // 2

            cnt = 0
            i = 0
            while i < len(nums) - 1 and cnt < p:
                if nums[i+1] - nums[i] <= mid:
                    i += 1
                    cnt += 1
                i += 1
            
            if cnt >= p:
                r = mid
            else:
                l = mid + 1
        
        return l