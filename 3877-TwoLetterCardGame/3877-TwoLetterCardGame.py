# Last updated: 11/10/2025, 7:59:59 PM
class Solution:
    def score(self, cards: List[str], x: str) -> int:
        freq_a = defaultdict(int)
        freq_b = defaultdict(int)
        for card in cards:
            if card[0] == x and card[1] != x:
                freq_a[card] += 1
            elif card[0] != x and card[1] == x:
                freq_b[card] += 1
        
        c = len([card for card in cards if card == x * 2])
        res = 0
        
        max_a = max(freq_a.values(), default=0)
        homogenous_pairsa = min(sum(freq_a.values()) // 2, sum(freq_a.values()) - max_a)
        res += homogenous_pairsa
        leftovera = sum(freq_a.values()) - 2 * homogenous_pairsa
        
        max_b = max(freq_b.values(), default=0)
        homogenous_pairsb = min(sum(freq_b.values()) // 2, sum(freq_b.values()) - max_b)
        res += homogenous_pairsb
        leftoverb = sum(freq_b.values()) - 2 * homogenous_pairsb
        

        # take care of stragglers
        if c > 0 and leftovera:
            temp = min(c, leftovera)
            c -= temp
            res += temp
        if c > 0 and leftoverb:
            temp = min(c, leftoverb)
            c -= temp
            res += temp

        if c > 0 and homogenous_pairsa:
            temp = min(homogenous_pairsa, c//2)
            c -= temp * 2
            res += temp
        if c > 0 and homogenous_pairsb:
            temp = min(homogenous_pairsb, c//2)
            c -= temp * 2
            res += temp
        return res

        