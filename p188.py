from functools import lru_cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if k > n//2:
            ans = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    ans += prices[i]-prices[i-1]
            return ans

        @lru_cache(None)
        def dfs(idx, k, buy=1):
            if idx > n-1 or k == 0:
                return 0
            ans = dfs(idx+1, k, buy)
            if buy:
                ans = max(ans, dfs(idx+1, k, 0) - prices[idx])
            else:
                ans = max(ans, dfs(idx+1, k-1, 1) + prices[idx])
            return ans

        return dfs(0, k)
