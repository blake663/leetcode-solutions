# Last updated: 11/10/2025, 7:59:48 PM
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = 10 ** 10
        
        @cache
        def go(index, left):
            if index == N:
                if left == 0:
                    return 0
                return INF
            if left == 0:
                return INF

            current = 0
            best = INF
            for i in range(index, N):
                current ^= nums[i]
                best = min(best, max(current, go(i+1, left-1)))
            return best

        return go(0, k)