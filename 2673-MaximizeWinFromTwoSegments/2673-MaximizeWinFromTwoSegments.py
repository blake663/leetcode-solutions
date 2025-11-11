# Last updated: 11/10/2025, 8:00:57 PM
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        if 2*k >= prizePositions[-1] - prizePositions[0]:
            return len(prizePositions)
        n = len(prizePositions)
        l = 0
        result = 0
        mx = [0] * (n + 1)

        for r, pos in enumerate(prizePositions): 
            while pos - prizePositions[l] > k:
                l += 1
            
            mx[r] = max(mx[r - 1], r - l + 1)
            result = max(result, mx[l - 1] + r - l + 1)
        return result
            

        
        