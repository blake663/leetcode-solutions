# Last updated: 11/10/2025, 7:59:42 PM
# 2**50 is and upper bound for n
MAX_BITS = 50

# number of bits = 4 => [{1}, {2, 4, 8}, {3, 5, 6, 9, 10, 12, 15}]
# numbers with i bit_count depth
reaches = [{1}]
for i in range(4):
    reaches.append(set())
    for bc in range(2, MAX_BITS+1):
        if bc.bit_count() in reaches[i]:
            reaches[-1].add(bc)

@cache
def count_comb(n, k):
    return math.comb(n, k)
    
class Solution:


    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0: return 1

        res = 0

        # check numbers less than n
        upper_ones = n.bit_count()
        for b in range(0, MAX_BITS):
            if n & 1<<b:
                upper_ones -= 1
                # set bit b to 0, count the number of ways to vary the lower bits to create a k-1 popcount-depth integer
                for num in reaches[k-1]:
                    if num >= upper_ones and b >= num - upper_ones:
                        res += count_comb(b, num - upper_ones)
                        if num == 1 and upper_ones == 0:
                            res -= 1 # don't include 0b00001 in the count

        # now check n
        if n.bit_count() in reaches[k-1] and n != 1:
            res += 1
            
        return res