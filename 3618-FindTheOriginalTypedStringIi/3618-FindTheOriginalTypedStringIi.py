# Last updated: 11/10/2025, 8:00:27 PM
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # T = len(word) - k
        MOD = 10**9 + 7

        groups = []
        is_group = False
        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                if is_group:
                    groups[-1] += 1
                else:
                    is_group = True
                    groups.append(1)
            else:
                is_group = False            
        
        ans = 1
        for group in groups:
            ans = (ans * (group + 1)) % MOD

        dp = [0] * (k)
        
        if len(word) - sum(groups) >= k:
            return ans

        dp[len(word) - sum(groups)] = 1
        
        for group in groups:
            j = max(0, k-1-group)
            window = sum(dp[j:])
            for i in range(k-1, -1, -1):
                num = dp[i]
                dp[i] = window
                if j > 0:
                    j -= 1
                    window = (window - num + MOD + dp[j]) % MOD
                else:
                    window = (window - num + MOD) % MOD   
        
        return (ans - sum(dp) + MOD) % MOD
        





























