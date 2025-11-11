# Last updated: 11/10/2025, 7:59:40 PM
class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        lengths = []

        res = []
        
        for c in s:
            lengths.append(length)
            if c == '*':
                if length:
                    length -= 1
            elif c == '#':
                length *= 2
            elif c == '%':
                pass #reverse
            else:
                length += 1

        if k >= length: return '.'

        # print(lengths)

        for c, l in (zip(s[::-1], lengths[::-1])):
            if c == '*':
            #     if length:
            #         length -= 1
                pass
            elif c == '#':
                # length *= 2
                if k >= l:
                    k -= l
            elif c == '%':
                k = l - k - 1
            else: # append letter
                # l -= 1
                if k == l: return c