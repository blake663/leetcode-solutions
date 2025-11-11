# Last updated: 11/10/2025, 8:00:42 PM
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        longest_side = max(nums)
        if longest_side >= sum(nums) - longest_side:
            return 'none'
        
        unique_count = len(set(nums))
        if unique_count == 3:
            return 'scalene'
        elif unique_count == 2:
            return 'isosceles'
        else:
            return 'equilateral'

        