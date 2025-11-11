# Last updated: 11/10/2025, 7:59:43 PM
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n, m = len(nums), max(nums)
        m_root = int(m**0.5)
        is_prime = [0] * (m+1)
        is_prime[0] = is_prime[1] = 1

        for i in range(2, m+1):
            if is_prime[i] == 0:
                for j in range(i*2, m+1, i):
                    is_prime[j] = i

        multiple = defaultdict(set)

        for i, num in enumerate(nums):
            x = num
            while is_prime[x] != 0 and x > 1:
                prime_factor = is_prime[x]
                multiple[prime_factor].add(i)
                while prime_factor == is_prime[x]:
                    x //= is_prime[x]
            if x > 1:
                multiple[x].add(i)
        
        visited = [False] * n
        visited[0] = True
        q = deque()
        steps = 0
        q.append(0)

        # print(multiple)
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                # print(x)
                if x == n-1:
                    return steps
                if x > 0 and not visited[x-1]:
                    q.append(x-1)
                    visited[x-1] = True
                if x+1 < n and not visited[x+1]:
                    q.append(x+1)
                    visited[x+1] = True
                num = nums[x]
                if is_prime[num] == 0:
                    for y in multiple[num]:
                        if visited[y]: continue
                        q.append(y)
                        visited[y] = True
                    multiple[num].clear()
            steps += 1
        return -1