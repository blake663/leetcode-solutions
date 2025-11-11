# Last updated: 11/10/2025, 8:00:55 PM
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count(x): # count pairs-sums less-than-or-equal-to x
            l, r = 0, len(nums) - 1
            cnt = 0
            for l, num in enumerate(nums):
                while l < r-1 and num + nums[r] > x:
                    r -= 1
                if num + nums[r] > x or l >= r:
                    break
                cnt += r - l
            return cnt
        
        return count(upper) - count(lower - 1)