# Last updated: 11/10/2025, 7:59:44 PM
class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c == '*':
                if res:
                    res.pop()
            elif c == '#':
                res.extend(list(res))
            elif c == '%':
                res = res[::-1]
            else:
                res.append(c)
        return ''.join(res)