# Last updated: 11/10/2025, 7:59:31 PM
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
#      a=5 b=6
# idea
        '''
            idea: min(|a - b|, |a + b|)  = ||a| - |b||
            idea: max(|a - b|, |a + b|)  =  |a| + |b|

            Let a = nums[i], b = nums[j]. Then:
            ||a| - |b|| <= min(|a|, |b|)
            ||a| + |b|| >= max(|a|, |b|) # always true???

            single sweep through array, cur = b, query for number of a's

            ex. b = 10, 
                case min(|a|, |b|) == |b|:
                    b <= a <= 2b # a in range [10,20]
                case min(|a|, |b|) == |a|:
                    b/2 <= a <= b

                in total:
                    count a in range [b/2, 2b]
                    
        '''

        seen = SortedList()
        cnt = 0

        for num in nums:
            num = abs(num)
            lo = seen.bisect_left(math.ceil(num/2))
            hi = seen.bisect_right(num*2)
            cnt += hi - lo
            seen.add(num)

        return cnt