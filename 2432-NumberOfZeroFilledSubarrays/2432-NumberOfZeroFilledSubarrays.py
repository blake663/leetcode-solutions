# Last updated: 11/10/2025, 8:01:05 PM
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count, total = 0, 0
        for num in nums:
            count = count + 1 if num == 0 else 0
            total += count
        return total