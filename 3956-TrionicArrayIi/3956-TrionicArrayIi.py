# Last updated: 11/10/2025, 7:59:32 PM
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        state = 0 # 0 => initial state, 1 => increasing, 2 => decreasing, 3 => increasing again
        sum1, sum2 = 0, 0
        initial_num = 0
        best = -math.inf

        for fst, snd in pairwise(nums):
            if snd - fst > 0:
                if state == 0:
                    state = 1
                    initial_num = fst
                    sum1 = fst + snd
                elif state == 1:
                    if initial_num < 0:
                        sum1 -= initial_num
                        initial_num = fst
                    sum1 += snd
                elif state == 2:
                    state = 3
                    initial_num = fst
                    sum2 = sum1 + snd
                    sum1 = fst + snd
                    if sum2 > best:
                        best = sum2
                elif state == 3:
                    if initial_num < 0:
                        sum1 -= initial_num
                        initial_num = fst
                    sum1 += snd
                    sum2 += snd
                    if sum2 > best:
                        best = sum2
            elif snd - fst < 0:
                if state > 0:
                    state = 2
                    sum1 += snd
            else:
                state = 0
        
        return best