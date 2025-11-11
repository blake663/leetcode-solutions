# Last updated: 11/10/2025, 8:00:05 PM
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def prefLen(lw, rw):
            ln = 0
            while ln < len(lw) and ln < len(rw) and lw[ln] == rw[ln]:
                ln += 1
            return ln
            
        def longestPref(l, r):
            res = 0
            ln = 0
            for i in range(l, r):
                ln = prefLen(words[i], words[i+1])
                res = max(res, ln)
            return res

        original_best = 0
        original_best_pos = 0

        for i in range(len(words)-1):
            ln = prefLen(words[i], words[i+1])
            if ln > original_best:
                original_best = ln
                original_best_pos = i

        arr = []

        for i in range(len(words)):
            # consider the prefix formed by removing words[i]
            cur = 0 if not (0 < i < len(words)-1) else prefLen(words[i-1], words[i+1])
            if i == original_best_pos or i == original_best_pos + 1:
                cur = max(cur, longestPref(0, i-1), longestPref(i+1, len(words)-1))
            else:
                cur = max(cur, original_best)
            arr.append(cur)

        return arr