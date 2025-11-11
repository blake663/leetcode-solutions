# Last updated: 11/10/2025, 8:00:08 PM
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        used = [False] * n
        placed = 0

        for amount in fruits:
            for i, capacity in enumerate(baskets):
                if amount <= capacity and not used[i]:
                    used[i] = True
                    placed += 1
                    break
        
        return n - placed