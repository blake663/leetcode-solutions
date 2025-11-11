# Last updated: 11/10/2025, 8:00:40 PM
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        best = len(word)
        freqs = Counter(word).values()
        

        mn, mx = min(freqs), max(freqs)

        if mx - mn <= k:
            return 0
        
        for lower in set(freqs):
            cost = 0
            for freq in freqs:
                if freq < lower:
                    cost += freq
                elif freq > lower + k:
                    cost += freq - lower - k
            best = min(best, cost)
        
        return best
