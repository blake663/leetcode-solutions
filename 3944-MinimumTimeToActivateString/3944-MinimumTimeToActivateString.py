# Last updated: 11/10/2025, 7:59:38 PM
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        if k > (n+1) * n // 2: return -1
        a = SortedList([-1,n])
        cnt = 0

        for i in range(n):
            ind = a.bisect_right(order[i])
            hi, lo = a[ind], a[ind-1]
            cnt += (order[i] - lo) * (hi - order[i])
            # print(cnt)
            if cnt >= k: return i
            a.add(order[i])

            