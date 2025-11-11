# Last updated: 11/10/2025, 8:00:52 PM
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        '''
            idea 1: bfs
                bounding the search space may be a problem
            idea 2: dp (unbounded knapsack)
                bounding also seems like a problem
            hint 1:
                If we want to make integer n equal to 0 by only subtracting powers of 2 from n, in how many operations can we achieve it?
                answer: we would need at least n.bitcount() many operations
            idea 3: check num2 binary composition with iteratively more steps
                consider ans == 1:
                    adjusted_num = (num1 - 1*num2)
                    if adjusted_num.bitcount() <= (i=1) <= adjusted_num:
                        return ans=1
                
        '''
        i = 1
        num1 -= num2
        while i <= num1:
            if num1.bit_count() <= i:
                return i
            i += 1
            num1 -= num2
            
        return -1