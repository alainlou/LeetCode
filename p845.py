from functools import lru_cache

class Solution:
    def longestMountain(self, A: List[int]) -> int:

        n = len(A)

        @lru_cache(None)
        def len_increasing(idx):
            if idx == n-1:
                return 0
            return (1 + len_increasing(idx+1)) if A[idx+1] < A[idx] else 0

        @lru_cache(None)
        def len_decreasing(idx):
            if idx == 0:
                return 0
            return (1 + len_decreasing(idx-1)) if A[idx-1] < A[idx] else 0

        ans = 0

        for i in range(n):
            calc1 = len_decreasing(i)
            calc2 = len_increasing(i)
            if calc1 > 0 and calc2 > 0:
                ans = max(ans, 1+calc1+calc2)

        return ans
