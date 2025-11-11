# Last updated: 11/10/2025, 8:00:21 PM
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        '''
            queries[i] = [l, r]
            operations:
                select a, b from array,
                replace with floor(a/4) and floor(b/4)
            number of operations needed for x = floor(log(4, x))

            time: O(n log(maxr)), space: O(1)
        '''
        # def count(l, r):
        #     res = 0
        #     base = 1
        #     while base <= l:
        #         res += r - l + 1
        #         base <<= 2
        #     while base <= r:
        #         res += r - base + 1
        #         base <<= 2
        #     return res

        tot = 0
        for l, r in queries:
            base = 1
            res = 0
            while base <= l:
                res += r - l + 1
                base <<= 2
            while base <= r:
                res += r - base + 1
                base <<= 2

            tot += (res + 1) // 2
        
        return tot