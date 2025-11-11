# Last updated: 11/10/2025, 8:00:23 PM
fmax = lambda l, r: l if l > r else r
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[0]]
        N = len(startTime)
        for i in range(1, N):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])

        res = 0

        suf = [0] * N
        for i in range(N-2, -1, -1):
            suf[i] = fmax(suf[i+1], gaps[i+2])
        
        pref = 0
        for i in range(N):
            res = fmax(res, gaps[i] + gaps[i+1])
            if i > 0 and pref < gaps[i-1]:
                pref = gaps[i-1]


            block_size = endTime[i] - startTime[i]
            # print(f'{i=}')
            if pref >= block_size or suf[i] >= block_size:
                res = fmax(res, gaps[i] + gaps[i+1] + block_size)



        return res
# ..11223334444444..55