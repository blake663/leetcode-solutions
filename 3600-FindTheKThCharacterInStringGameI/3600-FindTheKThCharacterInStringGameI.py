# Last updated: 11/10/2025, 8:00:30 PM
class Solution:
    def kthCharacter(self, k: int) -> str:
        cnt = 0
        k -= 1
        while k:
            print(k, log(k))
            k -= 2 ** math.floor(log2(k))
            cnt += 1
        
        return chr(ord('a') + cnt % 26)