# Last updated: 11/10/2025, 8:00:51 PM
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique = len(set(nums))
        freq = Counter()
        left = 0
        res = 0

        for num in nums:
            freq[num] += 1
            if len(freq) == unique:
                while freq[nums[left]] > 1:
                    freq[nums[left]] -= 1
                    left += 1
                res += left + 1
        return res