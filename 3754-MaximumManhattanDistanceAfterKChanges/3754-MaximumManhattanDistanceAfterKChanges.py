# Last updated: 11/10/2025, 8:00:15 PM
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        best = 0
        lat, lon = 0, 0
        for i in range(len(s)):
            if s[i] == 'W': lat += 1
            elif s[i] == 'E': lat -= 1
            elif s[i] == 'N': lon += 1
            else: lon -= 1
            dist = abs(lat) + abs(lon)
            best = max(best, min(dist + 2 * k, i+1))
        return best
