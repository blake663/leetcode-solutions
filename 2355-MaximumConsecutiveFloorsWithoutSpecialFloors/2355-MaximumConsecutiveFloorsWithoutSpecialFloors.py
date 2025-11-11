# Last updated: 11/10/2025, 8:01:20 PM
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        res = 0
        special = [bottom-1] + sorted(special) + [top+1]
        for a, b in zip(special[:-1], special[1:]):
            res = max(res, b-a-1)
        
        return res