# Last updated: 11/10/2025, 8:01:02 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = 0

        cur, best = 0, 0
        contiguous = False
        # just some micro-optimisations now
        for num in nums:
            if num == m and contiguous:
                cur += 1
            elif num >= m:
                best = 1 if num > m else best
                cur = 1
                m = num
                contiguous = True
            else:
                if cur > best:
                    best = cur
                cur = 0
                contiguous = False
        if cur > best:
            best = cur
        return best