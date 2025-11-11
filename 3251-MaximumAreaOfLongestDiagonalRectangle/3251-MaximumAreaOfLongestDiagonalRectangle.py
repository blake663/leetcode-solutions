# Last updated: 11/10/2025, 8:00:46 PM
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag, area = max((length**2 + width**2, length * width) for length, width in dimensions)
        return area