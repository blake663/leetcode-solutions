# Last updated: 11/10/2025, 8:01:07 PM
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        sieve = [0] * (maxValue + 1) # smallest prime factor
        for p in range(2, maxValue+1):
            if sieve[p] == 0:
                for f in range(p, maxValue+1, p):
                    if sieve[f] == 0:
                        sieve[f] = p
        
        res = 0

        for k in range(1, maxValue+1):
            cnt, prev = 0, -1
            x = k
            partial = 1
            while x > 1:
                if sieve[x] == prev:
                    cnt += 1
                else:
                    partial = (partial * math.comb(n+cnt-1, cnt)) % MOD
                    prev = sieve[x]
                    cnt = 1
                x //= sieve[x]
            partial = (partial * math.comb(n+cnt-1, cnt)) % MOD
            res = (res + partial) % MOD
            
        return res

    
    # choose i+1 