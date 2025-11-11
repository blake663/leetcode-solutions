# Last updated: 11/10/2025, 7:59:42 PM
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        N = len(nums)
        is_prime = [True] * (N+1)
        # prime_set = set()
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, N+1):
            if is_prime[i]:
                # prime_set.add(i)
                for j in range(i*2, N+1, i):
                    is_prime[j] = False

        # print(prime_set)
        sum_a, sum_b = 0, 0
        for i, num in enumerate(nums):
            if is_prime[i]:
                print('added to A ', num)
                sum_a += num
            else:
                sum_b += num

        return abs(sum_a - sum_b)
        