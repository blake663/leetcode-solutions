# Last updated: 11/10/2025, 8:00:34 PM
fmax = lambda l, r: l if l > r else r
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        dp = [0] * k

        for tot in range(k):
            for i in range(k):
                dp[i] = 0
            for num in nums:
                b = num % k
                a = (tot - b + k) % k
                tmp = dp[a] + 1
                if tmp > dp[b]:
                    dp[b] = tmp
                    res = fmax(res, tmp)
        
        return res