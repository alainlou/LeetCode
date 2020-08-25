from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def dfs(n):
            if n <= 2:
                return n
            return min(n%3+dfs(n//3), n%2+dfs(n//2))+1

        return dfs(n)
