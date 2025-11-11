# Last updated: 11/10/2025, 8:00:47 PM
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        count = 0

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, par):
            nonlocal count
            summ = values[node]

            for nei in adj[node]:
                if nei == par: continue
                summ += dfs(nei, node)
            
            summ %= k
            if summ == 0:
                count += 1
            return summ
        
        dfs(0, -1)

        return count
