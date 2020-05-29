from functools import lru_cache

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        @lru_cache(None)
        def dp(idx1, idx2):
            if idx1 >= len(A) or idx2 >= len(B):
                return 0
            tmp = 1 + dp(idx1+1, idx2+1) if A[idx1] == B[idx2] else dp(idx1+1, idx2+1)
            return max(tmp, dp(idx1+1, idx2), dp(idx1, idx2+1))

        return dp(0, 0)
