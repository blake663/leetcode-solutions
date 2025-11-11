# Last updated: 11/10/2025, 7:59:57 PM
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        # 3^19 ~= 1e9, so brute force would TLE
        ans = -math.inf
        n = len(nums)
        ZERO_OF_AND = 0xffffffff
        nums.sort(reverse=True)

        bsums = [0] * (2**n)
        bsums[0] = 0xffffffff

        for i in range(2**n):
            cur = 0
            if i:
                hi = int(math.log2(i))
                cur = nums[hi] & bsums[i & ~(1<<hi)]
                # print(i, hi, i& ~hi)
                bsums[i] = cur
            # print(cur)

            s = 0
            for b in range(n):
                if 1<<b & i: continue
                s ^= nums[b]
            
            x = 0
            # form a xor basis
            # https://usaco.guide/adv/xor-basis?lang=cpp#solution
            basis = []
            for b in range(n):
                if not 1<<b & i:
                    num = nums[b] & ~s
                    for base in basis:
                        num = min(num, num ^ base)
                    if num != 0:
                        basis.append(num)
            
            a = 0
            # This part is magic. We're able to find the max element in the space without trying all combinations.
            # It has something to do with it being an ordered basis.
            for base in basis:
                a = max(a, a ^ base)
            
            ans = max(ans, cur + s + 2 * a)

        return ans
