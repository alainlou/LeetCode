from collections import defaultdict
from functools import lru_cache

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        adj = defaultdict(set)

        for f in flights:
            adj[f[0]].add((f[1], f[2]))

        @lru_cache(None)
        def dfs(s, d, k):
            if s == d:
                return 0 if k >= 0 else float('inf')
            if k <= 0:
                return float('inf')
            ans = float('inf')
            for a in adj[s]:
                ans = min(ans, a[1] + dfs(a[0], d, k-1))
            return ans

        ret = dfs(src, dst, K+1)
        return ret if ret != float('inf') else -1
