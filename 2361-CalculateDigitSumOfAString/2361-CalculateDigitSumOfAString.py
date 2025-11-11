# Last updated: 11/10/2025, 8:01:18 PM
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ss = ''
            for i in range(0,len(s),k):
                ss += str(sum(int(c) for c in s[i:i+k]))
            s = ss
        return s