# Last updated: 11/10/2025, 7:59:54 PM
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # [
        # [1,3,3],
        # [2,5,4],
        # [4,3,5]]
        # , k = 2
        def get_sorted_cells(dp, m, n):
            sorted_cells = sorted([grid[i][j], dp[i][j], i, j] for i in range(m) for j in range(n))
            for i in range(m*n-2, -1, -1):
                sorted_cells[i][1] = min(sorted_cells[i][1], sorted_cells[i+1][1])
            return sorted_cells
        
        m, n = len(grid), len(grid[0])
        dp = None
        best = math.inf

        for p_cnt in range(k + 1): # 1
            prev_dp = dp
            # [ 0, 3, 6]
            # [ 2, 7,10]
            # [ 6, 9,14]
            dp = [[math.inf] * n for _ in range(m)]
            # [ 0,oo,oo]
            # [oo,oo,oo]
            # [oo,oo,oo]
            dp[0][0] = 0
            if p_cnt:
                sorted_cells = get_sorted_cells(prev_dp, m, n)
                # (1,0,0,0),(2,2,1,0),(3,3,0,1),(3,9,2,1),(3,6,0,2),(4,6,2,0),(4,10,1,2),(5,14,2,2),(5,7,1,1)
                # (1,0,0,0),(2,2,1,0),(3,3,0,1),(3,6,2,1),(3,6,0,2),(4,6,2,0),(4,7,1,2),(5,7,2,2),(5,7,1,1)
            for i in range(m): # 0
                for j in range(n): # 0
                    if i > 0:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
                    if p_cnt > 0:
                        idx = bisect_left(sorted_cells, grid[i][j], key=lambda x: x[0])
                        if idx < m*n:
                            dp[i][j] = min(dp[i][j], sorted_cells[idx][1])
            best = min(best, dp[m-1][n-1])


            # sorted_cells = get_sorted_cells(dp, m, n)
        return best

        