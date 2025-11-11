# Last updated: 11/10/2025, 7:59:53 PM
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[[None] * 3 for ii in range(len(prices))] for c in range(k+1)]
        # @cache
        def go(cnt, i, type): # type 1: holding, type -1: short
            if i >= len(prices):
                return 0
            if cnt > k:
                return 0
            if dp[cnt][i][type+1] != None:
                return dp[cnt][i][type+1]

            res = 0

            # print(cnt, i, type, res)
            if type == 0:
                res = max(go(cnt+1, i+1, 1), go(cnt+1, i+1, -1), go(cnt, i+1, 0))
            else:
                res = max(go(cnt, i+1, type), go(cnt, i+1, 0))

            if i > 0:
                # print(f'res += (prices[i] - prices[i-1]) * type = ', (prices[i] - prices[i-1]) * type)
                res += (prices[i] - prices[i-1]) * type

            dp[cnt][i][type+1] = res
            return res
        return go(0, 0, 0)