# Last updated: 11/10/2025, 8:00:37 PM
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        min_row, max_row = 0, M-1
        min_col, max_col = 0, N-1

        while min_row < max_row:
            for c in range(min_col, max_col+1):
                if grid[min_row][c]: break
            else:
                min_row += 1
                continue
            break

        while min_col < max_col:
            for r in range(min_row, max_row+1):
                if grid[r][min_col]: break
            else:
                min_col += 1
                continue
            break
        
        while min_col < max_col:
            for r in range(min_row, max_row+1):
                if grid[r][max_col]: break
            else:
                max_col -= 1
                continue
            break
        
        while min_row < max_row:
            for c in range(min_col, max_col+1):
                if grid[max_row][c]: break
            else:
                max_row -= 1
                continue
            break
                

        return (max_col - min_col + 1) * (max_row - min_row + 1)