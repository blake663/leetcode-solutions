# Last updated: 11/10/2025, 8:01:11 PM
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = [list() for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # count pairs in complete graph of size k
        def count_pairs(k):
            return (k-1) * k // 2

        visited = [False] * n

        def dfs(x):
            if visited[x]: return 0
            visited[x] = True
            res = 1
            for nei in adj[x]:
                if visited[nei]: continue
                res += dfs(nei)
            return res
        
        possible_pairs = count_pairs(n) # possible pairs

        reachable_pairs = 0

        for i in range(n):
            component_size = dfs(i)
            if component_size:
                reachable_pairs += count_pairs(component_size)
        
        return possible_pairs - reachable_pairs