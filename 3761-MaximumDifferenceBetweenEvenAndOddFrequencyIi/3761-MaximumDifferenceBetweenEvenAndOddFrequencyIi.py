# Last updated: 11/10/2025, 8:00:16 PM
fmax = lambda l, r: l if l > r else r
fmin = lambda l, r: l if l < r else r
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        res = -math.inf
        digits = set(s)
        for a in digits:
            for b in digits:
                if a == b: continue
                num_a2, num_b2 = 0, 0
                
                best = [[0,math.inf], [math.inf,math.inf]]
                
                num_a1, num_b1 = 0, 0
                j = 0

                for i in range(len(s)):
                    if s[i] == a:
                        num_a2 += 1
                    elif s[i] == b:
                        num_b2 += 1
                    
                    while i-j+1 > k:
                        if s[j] == a:
                            if num_a2 - num_a1 -1 >= 1:
                                num_a1 += 1
                                best[num_a1&1][num_b1&1] = fmin(best[num_a1&1][num_b1&1], num_a1 - num_b1)
                                j += 1
                            else:
                                break
                        elif s[j] == b:
                            if num_b2 - num_b1 -1 >= 2:
                                num_b1 += 1
                                best[num_a1&1][num_b1&1] = fmin(best[num_a1&1][num_b1&1], num_a1 - num_b1)
                                j += 1
                            else:
                                break
                        else:
                            j += 1
                    
                    if num_a2 >= 1 and num_b2 >= 2 and i-j+1 >= k:
                        res = fmax(res, num_a2 - num_b2 - best[(num_a2+1)&1][num_b2&1])


      
        return res
                