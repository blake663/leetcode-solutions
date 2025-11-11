# Last updated: 11/10/2025, 8:00:18 PM
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)

        for c in range(1, N):
            r = 0
            values = []
            for i in range(N - c):
                values.append(grid[r+i][c+i])
            values.sort()
            for i in range(N - c):
                grid[r+i][c+i] = values[i]
        
        for r in range(N):
            c = 0
            values = []
            for i in range(N - r):
                values.append(grid[r+i][c+i])
            values.sort(reverse=True)
            for i in range(N - r):
                grid[r+i][c+i] = values[i]
        
        return grid