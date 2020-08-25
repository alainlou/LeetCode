from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dfs(idx):
            if idx > len(prices) - 1:
                return 0

            ans = 0
            lo = prices[idx]

            for i in range(idx+1, len(prices)):
                ans = max(ans, prices[i] - lo + dfs(i+2))
                lo = min(lo, prices[i])

            return ans

        return dfs(0)
