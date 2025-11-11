# Last updated: 11/10/2025, 8:00:07 PM
class SegmentTree:
    def __init__(self, arr):
        rounded_length = 1 << math.ceil(math.log2(len(arr)))
        while len(arr) < rounded_length:
            arr.append(0)
        self.arr = [0] * rounded_length + arr
        self.n = rounded_length

        for i in range(self.n-1, 0, -1):
            self.arr[i] = max(self.arr[i*2], self.arr[i*2+1])
            
    def query(self, x):
        i = 1
        while i < self.n:
            if self.arr[2*i] >= x:
                i = 2 * i
            else:
                i = 2 * i + 1
        
        return i - self.n if self.arr[i] >= x else -1

    def delete(self, i):
        i += self.n
        self.arr[i] = 0

        while i > 1:
            i >>= 1
            self.arr[i] = max(self.arr[i*2], self.arr[i*2+1])

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # indexing by capacity would be trecherous: index compression, mapping amounts to capacities, etc
        # maintain basket order, index by order, store max
        res = 0
        tree = SegmentTree(baskets)

        for amount in fruits:
            pos = tree.query(amount)
            if pos != -1:
                tree.delete(pos)
            else:
                res += 1
        return res