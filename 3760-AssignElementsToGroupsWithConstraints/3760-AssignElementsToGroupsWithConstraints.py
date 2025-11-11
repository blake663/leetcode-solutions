# Last updated: 11/10/2025, 8:00:15 PM
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        max_g = max(groups)
        best = defaultdict(lambda: -1)

        for pos, num in enumerate(elements):
            if num not in best:
                for j in range(num, max_g+1, num):
                    if j not in best:
                        best[j] = pos

        return [best[group] for group in groups]