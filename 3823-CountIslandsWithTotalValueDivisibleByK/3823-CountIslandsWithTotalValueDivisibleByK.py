# Last updated: 11/10/2025, 8:00:04 PM
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if grid[r][c] == 0:
                return 0

            res = grid[r][c]
            grid[r][c] = 0

            if r > 0:
                res += dfs(r-1, c)
            if r+1 < ROWS:
                res += dfs(r+1, c)
            if c > 0:
                res += dfs(r, c-1)
            if c+1 < COLS:
                res += dfs(r, c+1)
            return res

        cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                value = dfs(r, c)
                if value > 0 and value % k == 0:
                    cnt += 1

        return cnt