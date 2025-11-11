# Last updated: 11/10/2025, 7:59:45 PM
fmax = lambda l, r: l if l > r else r
fmin = lambda l, r: l if l < r else r

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        adj = defaultdict(list)
        # g = [[False] * n for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            # g[a][b] = True
            # g[b][a] = True

        
        # dp = [[[False] * n for _ in range(n)] for _ in range(1<<n)]

        res = 1

        @cache
        def dfs(visited, u, v) -> int:
            mx = 0

            for u1 in adj[u]:
                if visited & 1<<u1: continue
                for v1 in adj[v]:
                    if visited & 1<<v1 or u1 == v1 or label[u1] != label[v1]: continue
                    if u1 < v1:
                        mx = fmax(mx, 2 + dfs(visited | 1<<u1 | 1<<v1, u1, v1))
                    else:
                        mx = fmax(mx, 2 + dfs(visited | 1<<u1 | 1<<v1, v1, u1))
                        

            return mx
        
        res = 0
        for u in range(n):
            # dp[1<<u][u][u] = True
            res = fmax(res, 1 + dfs(1<<u, u, u))
        
        for u, v in edges:
            if label[u] == label[v]:
                if u < v:
                    res = max(res, 2 + dfs(1<<u|1<<v, u, v))
                else:
                    res = max(res, 2 + dfs(1<<u|1<<v, v, u))




        return res

