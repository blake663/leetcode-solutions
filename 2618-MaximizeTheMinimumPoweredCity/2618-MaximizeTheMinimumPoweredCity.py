# Last updated: 11/10/2025, 8:00:58 PM
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        sums = [0] * n

        j = 0
        s = 0
        for i in range(n):
            while j < n and j <= i + r:
                s += stations[j]
                j += 1
            
            if i - r - 1 >= 0:
                s -= stations[i-r-1]
            sums[i] = s
        
        def valid(power):
            current, total = 0, 0
            q = Deque()
            for i in range(n):
                if len(q) > 2 * r:
                    current -= q[0]
                    q.popleft()
                if sums[i] + current < power:
                    q.append(power - (sums[i] + current))
                    current += q[-1]
                    total += q[-1]
                    if total > k: return False
                else:
                    q.append(0)
            
            return True

        left = min(sums)
        right = left + k

        while left < right:
            mid = math.ceil((left + right) / 2)

            if valid(mid):
                left = mid
            else:
                right = mid - 1
        
        return left