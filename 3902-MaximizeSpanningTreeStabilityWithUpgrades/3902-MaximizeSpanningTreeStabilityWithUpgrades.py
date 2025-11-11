# Last updated: 11/10/2025, 7:59:51 PM
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        par = [i for i in range(n)]
        size = [1 for _ in range(n)]

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(u, v):
            u = find(u)
            v = find(v)
            if u == v:
                return False

            if size[u] > size[v]:
                u, v = v, u

            # u under v
            par[u] = v
            size[v] += size[u]
            return True

        min_must = 1e8
        
        optional_edges = []
        for a, b, w, m in edges:
            if m:
                if not union(a, b):
                    return -1
                min_must = min(min_must, w)
            else:
                optional_edges.append([a,b,w])

        optional_edges.sort(key=lambda x: x[2], reverse=True)

        used = []
        for a, b, w in optional_edges:
            # print(par)
            if union(a, b):
                # print(f'append {(a,b,w)}')
                used.append(w)

        for i in range(max(0, len(used)-k), len(used)):
            used[i] = 2 * used[i]

        # print(par)

        if len(set(find(x) for x in par)) > 1:
            return -1

        return min(used + [min_must])

# fixed incorrect union find implementation
