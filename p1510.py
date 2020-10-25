from functools import lru_cache
from math import sqrt

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(n):
            if n == 0:
                return False
            for i in range(1, int(sqrt(n))+1):
                if not dfs(n-i*i):
                    return True
            return False

        return dfs(n)
