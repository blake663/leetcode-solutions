# Last updated: 11/10/2025, 8:00:02 PM
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        '''
        use dfs with an adjacency list to identify components.
        label each node by compenent (in an array)

        maintain isOnline[node_id]: Boolean[] and min_heaps[component_id]

        min_heaps can be updated lazily on read

        time: O(V + E + Q * log(V)), space: O(V + E)
        '''


        is_online = [True] * (c+1)
        component = [0] * (c+1)
        min_heaps = defaultdict(list)

        adj = [[] for _ in range(c+1)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(x, id):
            if component[x] != 0:
                return
            
            component[x] = id
            min_heaps[id].append(x)
            for y in adj[x]:
                dfs(y, id)
        
        id = 1
        for i in range(c):
            if component[i] == 0:
                dfs(i, id)
                id += 1
        
        # heapify the min_heaps
        for heap in min_heaps.values():
            heapq.heapify(heap)
        
        res = []

        for q_type, idx in queries:
            if q_type == 1:
                if is_online[idx]:
                    res.append(idx)
                else:
                    id = component[idx]
                    while min_heaps[id] and not is_online[min_heaps[id][0]]:
                        heapq.heappop(min_heaps[id])
                    if min_heaps[id]:
                        res.append(min_heaps[id][0])
                    else:
                        res.append(-1)
            else: # q_type == 2
                is_online[idx] = False
        
        return res