# Last updated: 11/10/2025, 8:01:09 PM
class SmallestInfiniteSet:

    def __init__(self):
        self.isPopped = [False] * (1001)
        self.nums = [num for num in range(1, 1001)]

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.nums)
        self.isPopped[smallest] = True
        return smallest

    def addBack(self, num: int) -> None:
        if self.isPopped[num]:
            self.isPopped[num] = False
            heapq.heappush(self.nums, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)