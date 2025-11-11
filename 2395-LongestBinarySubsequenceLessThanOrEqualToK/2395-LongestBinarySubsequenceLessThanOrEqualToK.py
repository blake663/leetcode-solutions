# Last updated: 11/10/2025, 8:01:13 PM
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        partition = len(s)
        num = 0
        place = 0
        while partition-1 >= 0 and num + (int(s[partition-1]) << place) <= k:
            partition -= 1
            num += int(s[partition]) << place
            place += 1
        
        return s[:partition].count('0') + len(s) - partition