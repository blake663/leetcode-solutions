# Last updated: 11/10/2025, 7:59:54 PM
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = [math.inf] * n
        dist[0] = 0
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w*2))

        q = [(0, 0)]

        while q:
            d, x = heapq.heappop(q)
            # print(d, x)

            if x == n - 1:
                return d

            for nei, w in adj[x]:
                if d + w < dist[nei]:
                    heapq.heappush(q, (d+w, nei))
                    dist[nei] = d + w

        return -1
            