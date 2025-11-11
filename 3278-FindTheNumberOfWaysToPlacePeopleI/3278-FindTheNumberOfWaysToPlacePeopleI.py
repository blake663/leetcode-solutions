# Last updated: 11/10/2025, 8:00:44 PM
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        rightmost = {}
        points.sort(key=lambda p: (p[0], -p[1]))
        # time: O(n * 50), space O(n) => O(50)

        i = 0 # 0
        ans = 0 # 0
        while i < len(points):
            stack = [] # 
            x = points[i][0] # 
            for y in range(50, -1, -1):
                if y in rightmost:
                    while stack and rightmost[y] >= stack[-1]:
                        stack.pop()
                    stack.append(rightmost[y])
                if points[i][1] == y:
                    ans += len(stack)
                    rightmost[y] = points[i][0]
                    stack = [x]
                    i += 1
                    if i == len(points) or points[i][0] != x:
                        break
        
        return ans
                

                