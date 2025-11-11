# Last updated: 11/10/2025, 8:00:55 PM
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        mins, maxs = [], []

        heapq.heapify(nums)
        for k in range(3):
            mins.append(heapq.heappop(nums))
        
        # reset and turn into max-heap
        nums.extend(mins)
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        
        for k in range(3):
            maxs.append(-heapq.heappop(nums))
        
        # print(mins, maxs)
                
        return min(maxs[i] - mins[2-i] for i in range(3))