from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dfs(i, j, k):
            if houses[i] != 0 and houses[i] != j:
                return float('inf')

            c = cost[i][j-1] if houses[i] != j else 0

            if i == 0:
                return c if k == 0 else float('inf')
            if k < 0:
                return float('inf')

            ans = float('inf')

            for l in range(1, n+1):
                ans = min(ans, dfs(i-1, l, k) if l == j else dfs(i-1, l, k-1))

            return ans + c

        best = float('inf')

        for i in range(1, n+1):
            best = min(best, dfs(m-1, i, target-1))

        return best if best != float('inf') else -1
