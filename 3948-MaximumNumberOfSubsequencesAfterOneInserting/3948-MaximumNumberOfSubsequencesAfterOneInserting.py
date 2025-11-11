# Last updated: 11/10/2025, 7:59:36 PM
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s) 
        pref = [[0,0,0] for _ in range(n+1)] # L(count), C(combinations), T(count)
        suff = [[0,0,0] for _ in range(n+1)]

        total = 0
        for i in range(n):
            pref[i+1] = list(pref[i])
            if s[i] == 'L':
                pref[i+1][0] += 1
            elif s[i] == 'C':
                pref[i+1][1] += pref[i][0]
            elif s[i] == 'T':
                total += pref[i][1]
                pref[i+1][2] += 1

        for i in range(n-1, -1, -1):
            suff[i] = list(suff[i+1])
            if s[i] == 'L':
                suff[i][0] += 1
            elif s[i] == 'C':
                suff[i][1] += suff[i+1][2]
            elif s[i] == 'T':
                suff[i][2] += 1

        res = max(total + pref[n][1], total + suff[0][1])

        for i in range(1, n):
            res = max(res, total + pref[i][0] * suff[i][2])

        return res