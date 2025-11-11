# Last updated: 11/10/2025, 8:00:26 PM
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        res = 0
        dq = Deque()
        dp = [0] * n
        dp[n-1] = fruits[0][n-1]
        for r in range(1, n-1):
            dp_next = [0] * n
            dq.clear()
            dq.append(0)
            dq.append(0)
            dq.append(dp[n-1])
            for c in range(n-1, max(n-1-r, r+1) - 1, -1):
                dq.append(dp[c-1])
                dq.popleft()
                dp[c] = fruits[r][c] + max(dq)
        
        res += dp[n-1]

        dp = [0] * n
        dp[n-1] = fruits[n-1][0]
        for c in range(1, n-1):
            dp_next = [0] * n
            dq.clear()
            dq.append(0)
            dq.append(0)
            dq.append(dp[n-1])
            for r in range(n-1, max(n-1-c, c+1) - 1, -1):
                dq.append(dp[r-1])
                dq.popleft()
                dp[r] = fruits[r][c] + max(dq)
        res += dp[n-1]
        res += sum(fruits[x][x] for x in range(n))
        return res