# Last updated: 11/10/2025, 8:00:35 PM
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        alt = 0
        prev = nums[0]&1^1
        evens = 0
        odds = 0

        for num in nums:
            is_odd = num&1
            if is_odd:
                odds += 1
            else:
                evens += 1
            if is_odd != prev:
                alt += 1
                prev = is_odd

        return max(evens, odds, alt)