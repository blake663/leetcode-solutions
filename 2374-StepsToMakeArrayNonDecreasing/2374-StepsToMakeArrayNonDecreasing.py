# Last updated: 11/10/2025, 8:01:14 PM
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        pp = [-1] * n
        for i in range(1, n):
            pp[i] = i - 1
        
        np = [-1] * n
        for i in range(0, n-1):
            np[i] = i + 1
        
        cur = set()
        next_round = set()
        cnt = 0

        for i in range(1, n):
            if nums[i-1] > nums[i]:
                cur.add(i)
        
        while cur:
            cnt += 1

            for idx in cur:
                np[pp[idx]] = np[idx]
                if np[idx] != -1:
                    pp[np[idx]] = pp[idx]
                    if nums[pp[idx]] > nums[np[idx]] and np[idx] not in cur:
                        next_round.add(np[idx])
            cur, next_round = next_round, set()
        
        return cnt



# [5,3,4,4, 7,3,6, 11,8,5, 11]