# Last updated: 11/10/2025, 8:01:16 PM
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0] == '$':
                try:
                    words[i] = '${:.2f}'.format(float(words[i][1:]) * (1-discount/100))
                except:
                    pass
        return ' '.join(words)