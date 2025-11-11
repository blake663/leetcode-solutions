# Last updated: 11/10/2025, 7:59:41 PM
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[[0, 0] for c in range(C)] for r in range(R)] # exit down, exit right
        dp[0][0] = [1, 1]

        for r in range(R):
            for c in range(C):
                if r:
                    if grid[r][c]:
                        dp[r][c][1] = dp[r-1][c][0]
                    else:
                        dp[r][c][1] = dp[r-1][c][0]
                        dp[r][c][0] = dp[r-1][c][0]
                if c:
                    if grid[r][c]:
                        dp[r][c][0] = dp[r][c-1][1]
                    else:
                        dp[r][c][1] += dp[r][c-1][1]
                        dp[r][c][1] %= 10**9 + 7
                        dp[r][c][0] += dp[r][c-1][1]
                        dp[r][c][0] %= 10**9 + 7

        return dp[R-1][C-1][0]