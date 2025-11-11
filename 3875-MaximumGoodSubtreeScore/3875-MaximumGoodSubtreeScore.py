# Last updated: 11/10/2025, 8:00:00 PM
fmax = lambda l, r: l if l > r else r

class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        # edges between nodes that share digits?
        n = len(vals)

        # dp[n][bitset = 2&&10 = 1024] = max score of subset using values from bitset only
        # dp = [[0] * 1024 for _ in range(n)]

        children = [list() for _ in range(n)]
        for i in range(n):
            if par[i] != -1:
                children[par[i]].append(i)
        
        ans = 0

        def dfs(i):
            nonlocal ans
            # for child in children[i]
            digits = Counter(int(c) for c in str(vals[i]))
            node_score = 0 if any(cnt > 1 for cnt in digits.values()) else vals[i]
            node_set = 0
            for d in digits:
                node_set |= 1<<d
            
            dp = {0: 0}
            dp[node_set] = node_score

            for child in children[i]:
                ch = dfs(child)
                for k1, v1 in ch.items():
                    if v1 == 0: continue
                    for k2, v2 in list(dp.items()):
                        if k1 & k2: continue
                        k3 = k1 | k2
                        dp[k3] = fmax(dp.get(k3, 0), dp[k2] + ch[k1])
            
            ans += max(dp.values())
            return dp
                    
        for i in range(n):
            if par[i] == -1:
                # print('dfs called on root = ', i)
                dfs(i)
                # print(dp[i])

        # for i, node in enumerate(dp):
        #     print(f'{i} max = {max(node)}')
            
        # return sum(max(node) for node in dp)
        return ans % (10**9 + 7)
            
