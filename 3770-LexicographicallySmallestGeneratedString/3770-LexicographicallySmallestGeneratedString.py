# Last updated: 11/10/2025, 8:00:10 PM
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)
        word = ['*'] * (N+M-1)
        for i in range(N):
            if str1[i] == 'T':
                for j in range(M):
                    if word[i+j] == '*':
                        word[i+j] = str2[j]
                    elif word[i+j] == str2[j]:
                        continue
                    else:
                        return ''

        # for i in range(N):
        #     if str1[i] == 'F':
        #         for j in range(M):
        #             if word[i+j] == '*':
        #                 word[i+j] = str2[j]
        #             elif word[i+j] == str2[j]:
        #                 continue
        #             else:
        #                 return ''
        #         else:
        
        # @cache
        def go(i, to_break):
            nonlocal word

            if i == N+M-1:
                return len(to_break) == 0
            
            for b in to_break:
                if i - b == M:
                    return False
            
            if i < N and str1[i] == 'F':
                to_break += (i,)

            if word[i] == '*':
                for c in range(2):
                    word[i] = chr(ord('a') + c)
                    tmp = []
                    for start in to_break:
                        if word[i] == str2[i-start]:
                            tmp.append(start)
                    if go(i+1, tuple(tmp)):
                        return True
                # print('false for word: ', word)
                word[i] = '*'
                return False

            else:
                tmp = []
                for start in to_break:
                    if word[i] == str2[i-start]:
                        tmp.append(start)
                return go(i+1, tuple(tmp))

        if go(0, ()):
            return ''.join(word)
        
        return ''

