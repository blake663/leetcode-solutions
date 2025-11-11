# Last updated: 11/10/2025, 7:59:58 PM
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        par = [i for i in range(n)]
        components = n

        def find(x):
            if par[x] == x:return x
            par[x] = find(par[x])
            return par[x]

        def union(u, v):
            nonlocal components
            u = find(u)
            v = find(v)
            if u == v: return False
            par[v] = u
            components -= 1
            return True

        edges.sort(key=lambda x: x[2])
        E = len(edges)

        prev = 0
        res = 0
        i = 0
        while components > k:
            prev = edges[i][2]
            
            while i < E and prev == edges[i][2]:
                union(edges[i][0], edges[i][1])
                i += 1

        return prev