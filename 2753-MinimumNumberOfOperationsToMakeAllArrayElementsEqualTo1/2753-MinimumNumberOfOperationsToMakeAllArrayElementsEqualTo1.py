# Last updated: 11/24/2025, 4:59:42 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        step 1:
            create an instance of '1' in the array.
        step 2:
            convert all remaining numbers to '1'
        
        step 1 is the hard part:
        how to find optimal number of moves? and how to detect when total gcd is not 1?


        aside: to find remainder between two numbers, use Chinese Remainder Theorem
        key insight: we can obtain the gcd of a length-k subarray by sweeping through in k-1 moves.

        step 1 now simply requires finding the minimum length of a subarray with gcd 1

        approach to find minimum subarray: sweep to end of array, starting at each index
        time: O(n^2), space: O(1)
        # '''

        # def gcd(a, b):
        #     if a < b:
        #         a, b = b, a
            
        #     while b != 0:
        #         a = a % b
        #         a, b = b, a
            
        #     return a
        
        best = math.inf

        for i in range(len(nums)):
            cur = nums[i]
            if cur == 1:
                best = 0
                break
            for j in range(i+1, min(len(nums), i+best)):
                cur = math.gcd(cur, nums[j])
                if cur == 1:
                    best = min(best, j-i)
                    break
        
        if best == math.inf:
            return -1
        elif best == 0:
            return sum(1 for num in nums if num != 1)
        else:
            return best + sum(1 for num in nums if num != 1) - 1
