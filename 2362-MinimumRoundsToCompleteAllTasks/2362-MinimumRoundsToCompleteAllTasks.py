# Last updated: 11/10/2025, 8:01:17 PM
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = dict()
        for x in tasks:
            if x not in freq.keys():
                freq[x] = 1
            else: freq[x] += 1
        
        cost = 0
        for v in freq.values():
            while v > 0:
                if v == 1:
                    return -1
                elif v == 4:
                    cost += 2
                    v -= 4
                else:
                    v -= 3
                    cost += 1
        
        return cost
        
        