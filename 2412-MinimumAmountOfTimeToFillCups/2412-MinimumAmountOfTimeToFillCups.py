# Last updated: 11/10/2025, 8:01:10 PM
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        result = 0
        amount.sort()
        while amount[2] > 0:
            amount[2] -= 1
            amount[1] -= 1
            amount.sort()
            result += 1
        
        return result
