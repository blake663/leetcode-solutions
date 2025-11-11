# Last updated: 11/10/2025, 8:01:12 PM
fmin = lambda l, r: l if l < r else r
fmax = lambda l, r: l if l > r else r
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [list() for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        best = math.inf
        subtree = [0] * n

        def find_subtrees(node, parent):
            subtree[node] = nums[node]
            for child in adj[node]:
                if child == parent: continue
                find_subtrees(child, node)
                subtree[node] ^= subtree[child]
        
        find_subtrees(0, -1)
        
        def try_second(node, parent, chosen, is_descendant):
            nonlocal best
            is_ancestor = False
            is_chosen = node == chosen
            for child in adj[node]:
                if child == parent: continue
                is_ancestor |= try_second(child, node, chosen, is_descendant or is_chosen)

            if is_chosen or is_ancestor:
                pass
            else:
                total, chosen_tree, cur_tree = subtree[0], subtree[chosen], subtree[node]
                if is_descendant:
                    vals = [total ^ chosen_tree, chosen_tree ^ cur_tree, cur_tree]
                    best = fmin(best, fmax(vals[0], fmax(vals[1], vals[2])) - fmin(vals[0], fmin(vals[1], vals[2])))
                else:
                    vals = [total ^ chosen_tree ^ cur_tree, chosen_tree, cur_tree]
                    best = fmin(best, fmax(vals[0], fmax(vals[1], vals[2])) - fmin(vals[0], fmin(vals[1], vals[2])))

            return is_ancestor or is_chosen
        
        for chosen in range(1, n):
            try_second(0, -1, chosen, False)

        return best