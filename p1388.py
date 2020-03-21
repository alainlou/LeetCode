from functools import lru_cache

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        @lru_cache(None)
        def solve(start, end, k, cycle = 0):
            if end - start + 1 < 1 + 2 *(k-1):
                return float('-inf')
            elif k == 1:
                return max(slices[start:end+1])
            return max(slices[start] + solve(start + 2, end - cycle, k - 1), \
                       solve(start + 1, end, k))

        n = len(slices)

        return solve(0, n-1, n//3, 1)
