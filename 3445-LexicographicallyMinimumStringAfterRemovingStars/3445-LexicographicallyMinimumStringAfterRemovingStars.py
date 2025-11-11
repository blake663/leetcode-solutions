# Last updated: 11/10/2025, 8:00:40 PM
class Solution:
    def clearStars(self, s: str) -> str:
        nearest = [[] for _ in range(26)]
        letters = set()
        smallest = 26
        deleted = set()

        for i, c in enumerate(s):
            if c == '*':
                while len(nearest[smallest]) == 0:
                    letters.remove(smallest)
                    smallest = min(letters)
                pos = nearest[smallest].pop()
                deleted.add(pos)
            else:
                chr_id = ord(c) - ord('a')
                nearest[chr_id].append(i)
                if smallest > chr_id:
                    smallest = chr_id
                letters.add(chr_id)
        
        return ''.join(c for i, c in enumerate(s) if c.isalpha() and i not in deleted)
        