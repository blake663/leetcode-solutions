# Last updated: 11/10/2025, 7:59:46 PM
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        INF = 10**14

        best_edges = defaultdict(lambda: -math.inf)
        for a, b, w in edges:
            if not online[a] or not online[b]: continue
            best_edges[a,b] = max(best_edges[a,b], w)

        adj = defaultdict(list)

        for (a, b), w in best_edges.items():
            adj[a].append((b, w))

        q = [(-INF, 0, 0)]
        dist = [INF] * n

        while q:
            score, cost, x = heapq.heappop(q)
            score *= -1

            if cost >= dist[x]: continue

            if x == n-1: return score

            dist[x] = cost

            for y, w in adj[x]:
                new_score = min(score, w)
                new_cost = cost + w
                if new_cost > k or new_cost == k and y != n-1: continue

                # it's okay to revisit nodes (with a >= cost), but only if it improves the score
                # if dist[y] <= new_cost:
                #     continue

                heapq.heappush(q, (-new_score, new_cost, y))
        
        return -1
