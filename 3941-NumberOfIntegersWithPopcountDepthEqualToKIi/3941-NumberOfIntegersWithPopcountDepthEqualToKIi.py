# Last updated: 11/10/2025, 7:59:39 PM
# class TreeNode:
#     __init__(self, )
# class SegmentTree:



class segment_tree:
    def __init__(self, arr):
        self.tree = [[0] * 6 for _ in range(4 * len(arr))]
        # in the constructor here we use zero indexed instead of one-indexed for curLeft, curRight and idx on update(),
        # since we are assuming the array for initialization is 0-indexed.
        # "cur" parameter is always 1 to ensure 1-indexing in the segment tree itself, however curLeft, curRight and idx can be
        # 0-indexed or 1-indexed relative to each other to be used for calculating segments.
        for i in range(len(arr)):
            self.update(1, 0, len(arr) - 1, i, arr[i])

    def update(self, cur, cur_left, cur_right, idx, de):
        # make sure we reach leaf node when the left interval equals right interval and return the value located in the tree
        if cur_left == cur_right and cur_left == idx:
            self.tree[cur] = de
        else:
            # compute value of the midpoint where we cut the segment in half
            cur_mid = (cur_left + cur_right) // 2
            # remember n * 2 is left child node and n * 2 + 1 is the right child node
            if idx <= cur_mid:
                self.update(cur * 2, cur_left, cur_mid, idx, de)
            else:
                self.update(cur * 2 + 1, cur_mid + 1, cur_right, idx, de)
            # after updating the values, compute the new value for the node
            # self.tree[cur] = self.tree[cur * 2] + self.tree[cur * 2 + 1]
            for i in range(6):
                self.tree[cur][i] = self.tree[cur * 2][i] + self.tree[cur * 2 + 1][i]

    def query(self, cur, cur_left, cur_right, query_left, query_right):
        # if our current left interval is greater than the queried right interval it means we are out of range
        # similarly, if the current right interval is less than the queried left interval we are out of range and in both cases return 0
        if cur_left > query_right or cur_right < query_left:
            return [0] * 6
        # check if we are in range, if we are return the current interval
        elif query_left <= cur_left and cur_right <= query_right:
            return self.tree[cur]
        # this means part of our interval is in range but part of our interval is not in range, we must therefore query both children
        cur_mid = (cur_left + cur_right) // 2
        l = self.query(cur * 2, cur_left, cur_mid, query_left, query_right)
        r = self.query(cur * 2 + 1, cur_mid + 1, cur_right, query_left, query_right)
        # print('query, join ', l, r)
        # return []
        return [a+b for a,b in zip(l, r)]

    def __repr__(self):
        return str(self.tree)



def dep(x):
    res = 0
    while x > 1:
        x = x.bit_count()
        res += 1
    return res

class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        depfs = [[0] * 6 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            bc = dep(nums[i])
            if bc < 6:
                depfs[i][bc] = 1
        tree = segment_tree(depfs)

        # tree.update(1, 0, len(nums)-1, 0, [0,0,0,0,0,0])
        # q = tree.query(1, 0, len(nums)-1, 0, 1)
        res = []
        for q in queries:
            # print('tree before: ', tree)
            if q[0] == 1:
                qr = tree.query(1, 0, len(nums)-1, q[1], q[2])
                # print(f'{qr=}')
                cnt = qr[q[3]]
                res.append(cnt)
            else:
                bc = dep(q[2])
                val = [0] * 6
                if bc < 6:
                    val[bc] = 1
                tree.update(1, 0, len(nums)-1, q[1], val)
                
        # print(q)
        return res