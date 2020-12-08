from collections import defaultdict
from functools import lru_cache

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        @lru_cache(None)
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n*factorial(n-1)

        def choose(n, k):
            return factorial(n)//(factorial(k)*factorial(n-k))

        mods = defaultdict(int)

        for t in time:
            mods[t%60] += 1

        ans = 0

        for k, v in mods.items():
            if k == 0 or k == 30:
                ans += choose(v, 2) if v >= 2 else 0
            elif k < 30 and 60-k in mods:
                ans += v*mods[60-k]

        return ans
