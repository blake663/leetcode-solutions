# Last updated: 11/10/2025, 8:00:38 PM
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def merge(area1, area2):
            if area1[0] == -1:
                return area2
            if area2[0] == -1:
                return area1
            
            # top, left, bottom, right
            t1, l1, b1, r1 = area1
            t2, l2, b2, r2 = area2
            return [min(t1, t2), min(l1, l2), max(b1, b2), max(r1, r2)]
        
        # top, left, bottom, right
        # dp = [[[[[-1,-1,-1,-1] for r in range(C)] for b in range(R)] for l in range(C)] for t in range(R)]

        @cache
        def find_rect(t, l, b, r):
            if t==b and l==r:
                return [t, l, b, r] if grid[t][l] else [-1,-1,-1,-1]
            
            if t==b:
                return merge(find_rect(t, l, b, l), find_rect(t, l+1, b, r))
            else:
                return merge(find_rect(t, l, t, r), find_rect(t+1, l, b, r))

        @cache
        def find_area(t, l, b, r):
            t2, l2, b2, r2 = find_rect(t, l, b, r)
            if t2 == -1:
                return math.inf
            return (b2 - t2 + 1) * (r2 - l2 + 1)
        
        best = R * C
        for r1 in range(R-1):
            for c in range(C-1):
                best = min(best, find_area(0, 0, r1, C-1) + find_area(r1+1, 0, R-1, c) + find_area(r1+1, c+1, R-1, C-1))
                best = min(best, find_area(r1+1, 0, R-1, C-1) + find_area(0, 0, r1, c) + find_area(0, c+1, r1, C-1))
            for r2 in range(r1+1, R-1):
                best = min(best, find_area(0, 0, r1, C-1) + find_area(r1+1, 0, r2, C-1) + find_area(r2+1, 0, R-1, C-1))
        
        for c1 in range(C-1):
            for r in range(R-1):
                best = min(best, find_area(0, 0, R-1, c1) + find_area(0, c1+1, r, C-1) + find_area(r+1, c1+1, R-1, C-1))
                best = min(best, find_area(0, c1+1, R-1, C-1) + find_area(0, 0, r, c1) + find_area(r+1, 0, R-1, c1))
            for c2 in range(c1+1, C-1):
                best = min(best, find_area(0, 0, R-1, c1) + find_area(0, c1+1, R-1, c2) + find_area(0, c2+1, R-1, C-1))
        
        return best
