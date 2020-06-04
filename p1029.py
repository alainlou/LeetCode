from functools import lru_cache

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        @lru_cache(None)
        def dfs(idx, balance):
            if idx == n:
                return 0 if balance == 0 else float('inf')
            return min(costs[idx][0] + dfs(idx+1, balance-1), costs[idx][1] + dfs(idx+1, balance+1))

        return dfs(0, 0)
