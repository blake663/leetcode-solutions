# Last updated: 11/10/2025, 7:59:55 PM
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        row = defaultdict(int)
        MOD = (10**9 + 7)
        for x, y in points:
            row[y] += 1

        rowvals = []
        for c in row.values():
            if c > 1:
                rowvals.append((c * (c-1) // 2) % MOD)

        if len(rowvals) < 2:
            return 0
        
        res = 0
        p = rowvals[0]
        for i in range(1, len(rowvals)):
            # print(i, j, rowvals[i], rowvals[j])
            res = (res + rowvals[i] * p) % MOD
            p = (p + rowvals[i]) % MOD

            

        return res