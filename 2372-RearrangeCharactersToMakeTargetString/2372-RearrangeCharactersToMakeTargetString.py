# Last updated: 11/10/2025, 8:01:16 PM


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sFreq = defaultdict(lambda: 0)
        for c in s:
            sFreq[c] = sFreq[c] + 1
        
        targetFreq = defaultdict(lambda: 0)
        for c in target:
            targetFreq[c] = targetFreq[c] + 1
        
        ans = 1000
        
        for ch, count in targetFreq.items():
            ans = min(ans, sFreq[ch] / count)
        
        return int(ans)