from functools import lru_cache

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:

        houses.sort()

        def pick(i, j):
            ret = 0
            med = houses[(i+j)//2] if (j-i)%2 == 0 else (houses[(i+j)//2]+houses[(i+j)//2 + 1])//2
            for k in range(i, j+1):
                ret += abs(houses[k] - med)
            return ret

        @lru_cache(None)
        def dfs(i, j, k):
            if k == 1:
                return pick(i, j)
            ans = float('inf')
            for l in range(i, j-k+2):
                ans = min(ans, dfs(i, l, 1) + dfs(l+1, j, k-1))
            return ans

        return dfs(0, len(houses)-1, k)
