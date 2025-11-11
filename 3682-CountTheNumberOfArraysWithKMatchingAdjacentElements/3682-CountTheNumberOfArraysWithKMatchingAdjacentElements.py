# Last updated: 11/10/2025, 8:00:24 PM
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        prod = m * pow(m-1, n - k - 1, MOD)

        # ncr = [0] * (k+1)
        # ncr[0] = 1
        ncr = comb(n-1, k)

        # for _ in range(n-1):
        #     for i in range(k, -1, -1):
        #         if i > 0:
        #             ncr[i] = int((ncr[i] + ncr[i-1]) % MOD)

        # def nCr(n, r):
    
        #     sum = 1

        #     # Calculate the value of n choose r 
        #     # using the binomial coefficient formula
        #     for i in range(1, r+1):
        #         sum = sum * (n - r + i) // i
            
        #     return sum

        return ncr * prod % MOD