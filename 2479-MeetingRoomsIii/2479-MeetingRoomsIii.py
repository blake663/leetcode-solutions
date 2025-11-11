# Last updated: 11/10/2025, 8:01:05 PM
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        meeting_count = [0] * n
        used, unused = [], [i for i in range(n)]

        for start, end in meetings:
            while used and used[0][0] <= start:
                room = heapq.heappop(used)[1]
                heapq.heappush(unused, room)

            if unused:
                room = heapq.heappop(unused)
                heapq.heappush(used, (end, room))
            else:
                prev_end, room = heapq.heappop(used)
                heapq.heappush(used, (prev_end + end - start, room))

            meeting_count[room] += 1

        
        # print(meeting_count)
        return meeting_count.index(max(meeting_count))