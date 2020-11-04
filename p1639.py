from collections import defaultdict
from functools import lru_cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        n = len(words[0])
        m = len(target)

        arr = [defaultdict(int) for _ in range(n)]

        for w in words:
            for i, c in enumerate(w):
                arr[i][c] += 1

        @lru_cache(None)
        def dfs(w_i, t_i):
            if t_i > m-1:
                return 1
            if w_i > n-1:
                return 0
            if n-w_i < m-t_i:
                return 0
            ans = dfs(w_i+1, t_i)
            if target[t_i] in arr[w_i]:
                ans += arr[w_i][target[t_i]]*dfs(w_i+1, t_i+1)
            return ans%mod

        return dfs(0, 0)
