# Last updated: 11/10/2025, 8:00:25 PM
fmax = lambda l, r: l if l > r else r

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        pq = [(0,0,0)]
        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 0

        while pq:
            d, i, j = heapq.heappop(pq)

            mt = 1 if (i^j)&1 == 0 else 2

            if i > 0 and dist[i-1][j] == -1:
                visitTime = fmax(d, moveTime[i-1][j]) + mt
                heapq.heappush(pq, (visitTime, i-1, j))
                dist[i-1][j] = visitTime
            if i+1 < m and dist[i+1][j] == -1:
                visitTime = fmax(d, moveTime[i+1][j]) + mt
                heapq.heappush(pq, (visitTime, i+1, j))
                dist[i+1][j] = visitTime
            if j > 0 and dist[i][j-1] == -1:
                visitTime = fmax(d, moveTime[i][j-1]) + mt
                heapq.heappush(pq, (visitTime, i, j-1))
                dist[i][j-1] = visitTime
            if j+1 < n and dist[i][j+1] == -1:
                visitTime = fmax(d, moveTime[i][j+1]) + mt
                heapq.heappush(pq, (visitTime, i, j+1))
                dist[i][j+1] = visitTime
        
        return dist[m-1][n-1]