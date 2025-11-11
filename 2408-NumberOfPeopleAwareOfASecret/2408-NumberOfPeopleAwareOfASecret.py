# Last updated: 11/10/2025, 8:01:11 PM
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        newly_active = [0] * n # 0,0,1,0,1,1
        removed = [0] * n      # 0,0,0,0,1,0

        if delay < n:
            newly_active[delay] = 1
        if forget < n:
            removed[forget] = 1

        total, active = 1, 0 # 5, 2

        for i in range(n): # 5
            active += newly_active[i]
            total -= removed[i]
            active -= removed[i]

            if i + delay < n:
                newly_active[i+delay] += active
            if i + forget < n:
                removed[i+forget] += active
            total += active
        
        return total % (10**9 + 7)