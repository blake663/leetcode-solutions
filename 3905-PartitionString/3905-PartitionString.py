# Last updated: 11/10/2025, 7:59:49 PM
class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []

        i = 0
        for j in range(len(s)):
            sub = s[i:j+1]
            if sub not in seen:
                res.append(sub)
                seen.add(sub)
                i = j + 1

        return res