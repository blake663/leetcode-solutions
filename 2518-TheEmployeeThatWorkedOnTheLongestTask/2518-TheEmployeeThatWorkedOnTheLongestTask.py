# Last updated: 11/10/2025, 8:01:01 PM
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        startTime = 0
        best, res = 0,1e4
        for id, endTime in logs:
            if endTime - startTime > best or (endTime - startTime == best and id < res):
                best = endTime - startTime
                res = id
            startTime = endTime
        
        return res