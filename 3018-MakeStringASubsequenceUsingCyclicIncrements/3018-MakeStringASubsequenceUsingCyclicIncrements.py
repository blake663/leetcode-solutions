# Last updated: 11/10/2025, 8:00:47 PM
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool: 
        match_len = 0
        for c in str1:
            a = ord(str2[match_len])
            b = ord(c)
            if (str2[match_len] == c or a == b + 1 or a == b - 25):
                match_len += 1
                if match_len == len(str2):
                    return True

        return False
