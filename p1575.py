from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7

        @lru_cache(None)
        def dfs(idx, fuel):
            ans = 0
            if idx == finish:
                ans += 1
            for i, l in enumerate(locations):
                if i != idx and abs(l - locations[idx]) <= fuel:
                    ans += dfs(i, fuel-abs(l - locations[idx]))
            return ans%mod

        return dfs(start, fuel)
