# Last updated: 11/10/2025, 8:00:45 PM
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        points.sort(key=lambda p: (p[0], -p[1]))

        for i in range(n):
            min_y = math.inf
            for j in range(i-1, -1, -1):
                if points[j][1] < points[i][1]:
                    continue
                if points[j][1] < min_y:
                    min_y = points[j][1]
                    ans += 1

        return ans