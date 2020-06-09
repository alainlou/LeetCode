from functools import lru_cache

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        @lru_cache(None)
        def dfs(idx1, idx2):
            if idx1 > len(s) - 1:
                return True
            if idx2 > len(t) - 1:
                return False
            if s[idx1] == t[idx2]:
                return dfs(idx1+1, idx2+1)
            return dfs(idx1, idx2+1)

        return dfs(0, 0)
