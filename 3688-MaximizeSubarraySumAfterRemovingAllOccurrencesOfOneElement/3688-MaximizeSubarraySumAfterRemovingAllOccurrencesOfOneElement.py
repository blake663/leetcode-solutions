# Last updated: 11/10/2025, 8:00:22 PM
class node:
    def __init__(self, val=0):
        self.pref = val
        self.suf = val
        self.sum = val
        self.mss = val
        self.disabled = False

    # def __repr__(self):
    #     return f"node({self.pref} {self.suf} {self.sum} {self.mss})"


class SegmentTree:
    def __init__(self, nums):
        self.T = 2**math.ceil(log2(len(nums)))
        self.tree = [node() for _ in range(self.T)]
        for i in range(self.T):
            if i < len(nums):
                self.tree.append(node(nums[i]))
            else:
                self.tree.append(node(-math.inf))
        
        for i in range(self.T-1, 0, -1):
            l, r = self.tree[i << 1], self.tree[i << 1 | 1]
            self.tree[i].pref = max(l.pref, l.sum + r.pref)
            self.tree[i].suf = max(r.suf, l.suf + r.sum)
            self.tree[i].sum = l.sum + r.sum
            self.tree[i].mss = max(l.mss, r.mss, l.suf + r.pref)

    def queryAll(self):
        return self.tree[1].mss

    def update(self, i, v):
        i += self.T
        self.tree[i] = node(v)
        i >>= 1
        while i:
            l, r = self.tree[i << 1], self.tree[i << 1 | 1]
            if l.sum == -math.inf:
                self.tree[i].pref = r.pref
            else:
                self.tree[i].pref = max(l.pref, l.sum + r.pref)
            if r.sum == -math.inf:
                self.tree[i].suf = l.suf
            else:
                self.tree[i].suf = max(r.suf, l.suf + r.sum)
            if l.sum == -math.inf:
                self.tree[i].sum = r.sum
            elif r.sum == -math.inf:
                self.tree[i].sum = l.sum
            else:
                self.tree[i].sum = l.sum + r.sum
            self.tree[i].mss = max(l.mss, r.mss, l.suf + r.pref)
            i >>= 1


    
class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        indexes = defaultdict(list)

        for i in range(len(nums)):
            indexes[nums[i]].append(i)
        
        if len(indexes) == 1:
            if nums[0] <= 0:
                return nums[0]
            else:
                return sum(nums)
        
        st = SegmentTree(nums)
        # return st.queryAll()

        best = st.queryAll()
        for x in indexes:
            # print(st.tree)
            for idx in indexes[x]:
                st.update(idx, -math.inf)
            # print(st.tree)
            best = max(best, st.queryAll())
            for idx in indexes[x]:
                st.update(idx, x)
            # print(st.tree)
            
        
        return best


# [node(0 0 0 0),                                               node(0 -inf -inf 4), 

#                          node(-1 -1 -4 2),                                                   node(4 -inf -inf 4), 
#         node(-1 2 -1 2),                   node(-2 -1 -3 -1),                     node(3 1 1 3),               node(3 -inf -inf 3), 
# node(-3 -3 -3 -3),  node(2 2 2 2), node(-2 -2 -2 -2), node(-1 -1 -1 -1), node(3 3 3 3), node(-2 -2 -2 -2), node(3 3 3 3), node(-inf -inf -inf -inf)]

# [node(0 0 0 0),                                                 node(0 -inf -inf 4), 
#                         node(-1 -1 -4 2),                                                       node(4 -inf -inf 4), 
#         node(-1 2 -1 2),                node(-2 -1 -3 -1),                      node(3 1 1 3),                  node(3 -inf -inf 3), 
# node(-3 -3 -3 -3), node(2 2 2 2), node(0 0 0 0), node(-1 -1 -1 -1),     node(3 3 3 3), node(0 0 0 0),       node(3 3 3 3), node(-inf -inf -inf -inf)]