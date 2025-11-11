# Last updated: 11/10/2025, 8:01:19 PM
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = []
        for x in candidates:
            p = 0
            while 1 << p <= x:
                if len(count) <= p:
                    count.append(0)
                if x & (1<<p) > 0:
                    count[p] += 1
                p+=1
            
        return max(count)