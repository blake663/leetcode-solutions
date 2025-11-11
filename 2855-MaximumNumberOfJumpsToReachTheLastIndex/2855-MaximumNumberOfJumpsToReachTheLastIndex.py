# Last updated: 11/10/2025, 8:00:50 PM
# I give credit to whatever megamind I copied this from. 

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.max_tree = [-math.inf] * self.n
        self.max_tree.extend(arr)
        for i in range(self.n-1, 0, -1):
            self.max_tree[i] = max(self.max_tree[i << 1], self.max_tree[i << 1 | 1])
    # update a single value
    def update(self, i, val):
        i += self.n
        self.max_tree[i] = val
        while i > 1:
            self.max_tree[i >> 1] = max(self.max_tree[i], self.max_tree[i^1])
            i >>= 1
    # query max value in range
    def max_val(self, l, r):
        maximum = -math.inf
        l += self.n
        r += self.n

        while l < r:
            if l&1:
                maximum = max(maximum, self.max_tree[l])
                l += 1
            if r&1:
                r -=1
                maximum = max(maximum, self.max_tree[r])
            
            l >>= 1
            r >>= 1
        return maximum




class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # T is a segment tree of the running max number of jumps to get to an instance 
        A = sorted(set(nums))
        T = SegmentTree(([-inf] * len(A)))
        T.update(bisect_left(A, nums[0]), 0)
        res = 0

        # iterate through all the numbers in order
        for n in nums[1:]:
            # find the range of numbers that it could be reached from
            a = n-target
            b = n+target
            # find the max in that range. only visited values will impact the value, otherwise stays at -math.inf
            res = T.max_val(bisect_left(A,a), bisect_right(A,b)) + 1
            # The number is set to its new max
            T.update(bisect_left(A,n), res)
        return res if res > -inf else -1
        