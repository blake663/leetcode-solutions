# Last updated: 11/10/2025, 8:00:32 PM
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # change to zero-indexed
        k -= 1
        res = 0
        for op in operations:
            if k&1 and op:
                res += 1
            k >>= 1
        return chr(ord('a') + res % 26)