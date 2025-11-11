# Last updated: 11/10/2025, 7:59:50 PM
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        evens = len([num for num in nums if num&1 == 0])
        odds = len(nums) - evens
        if abs(odds - evens) > 1:
            return -1

        if odds == evens:
            cost1 = 0
            e1 = 1
            cost2 = 0
            e2 = 0
            for i, num in enumerate(nums):
                if num&1 == 0:
                    cost1 += abs(e1 - i)
                    cost2 += abs(e2 - i)
                    e1 += 2
                    e2 += 2
            
            return min(cost1, cost2)
        else:
            cost = 0
            e = 1 if odds > evens else 0
            for i, num in enumerate(nums):
                if num&1 == 0:
                    cost += abs(e - i)
                    e += 2
            return cost
