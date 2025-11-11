# Last updated: 11/10/2025, 8:00:20 PM
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)
        gaps = [startTime[0]] + [startTime[i+1] - endTime[i] for i in range(N-1)] + [eventTime - endTime[-1]]

        window = sum(gaps[:k+1])
        res = window

        for i in range(N-k):
            window -= gaps[i]
            window += gaps[i+k+1]
            res = max(res, window)
        
        return res