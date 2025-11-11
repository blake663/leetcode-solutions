# Last updated: 11/10/2025, 8:00:56 PM
# copypasta
class Solution:
    def minCost(self, basket1, basket2):
        count = Counter()
        global_min = float('inf')

        # Step 1: Count items and track global min
        for x in basket1:
            count[x] += 1
            global_min = min(global_min, x)
        for x in basket2:
            count[x] -= 1
            global_min = min(global_min, x)

        total = 0

        # Step 2: Check if balancing is possible
        for v in count.values():
            if v % 2 != 0:
                return -1  # odd difference means not swappable
            total += abs(v)

        # Step 3: Build swap list
        im = []
        for num, v in count.items():
            im.extend([num] * (abs(v) // 2))

        # Step 4: Sort swap list
        im.sort()

        # Step 5: Choose cheapest swaps
        half = len(im) // 2
        double_min = 2 * global_min
        ans = sum(min(im[i], double_min) for i in range(half))

        # Step 6: Return result
        return ans 