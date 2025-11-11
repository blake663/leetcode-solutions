# Last updated: 11/10/2025, 7:59:51 PM
# credit to https://leetcode.com/problems/count-number-of-trapezoids-ii/solutions/6980360/o-n-2-python-4-seen-line-indices
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        PRECISION = 8

        # We can't bucket only by line segment length or only by intercept
        # we need to count the lines with the same length and different intercept as parallelograms,
        # and we need to count the lines with a different length and different intercept as trapezoids.
        # We need to use a weird trick to calculate the count of same length, different intercept by
        # finding same_length - same_length_same_b = same_length_dif_b

        total = defaultdict(int)
        same_len = defaultdict(int)
        same_b = defaultdict(int)
        same_len_same_b = defaultdict(int)

        p_count, t_count = 0, 0

        for i in range(n):
            for j in range(i+1, n):
                p1, p2 = points[i], points[j]
                dy, dx = p2[1]-p1[1], p2[0]-p1[0]
                if dx < 0 or dx == 0 and dy < 0:
                    dy, dx = -dy, -dx
                g = gcd(dy, dx) or 1
                m = (dy//g,dx//g)
                l = max(dy, dx) # we must have one positive value unless at origin, so max unique enough
                b = p1[1] * m[1] - m[0] * p1[0]
                
                if total[m]:
                    dif_len = total[m] - same_len[(m,l)]
                    dif_b = total[m] - same_b[(m,b)]
                    same_len_dif_b = same_len[(m,l)] - same_len_same_b[(m,l,b)]
                    p_count += same_len_dif_b
                    t_count += dif_b - same_len_dif_b
                
                total[m] += 1
                same_len[(m,l)] += 1
                same_b[(m,b)] += 1
                same_len_same_b[(m,l,b)] += 1

        return p_count // 2 + t_count



#                 has same len                has dif len


# has same b      0                           0




# has dif b       par                         trap

