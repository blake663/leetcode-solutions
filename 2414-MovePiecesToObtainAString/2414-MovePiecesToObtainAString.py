# Last updated: 11/10/2025, 8:01:08 PM
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if ''.join(c for c in start if c != '_') != ''.join(c for c in target if c != '_'):
            return False
        
        target_indexes = []

        for i in range(len(target)):
            if target[i] != '_':
                target_indexes.append(i)
        
        j = 0

        for i, c in enumerate(start):
            if c == '_': continue
            elif c == 'L':
                if i < target_indexes[j]:
                    return False
            else:
                if i > target_indexes[j]:
                    return False
            j += 1
        return True