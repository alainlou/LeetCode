from functools import lru_cache

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 10**9 + 7

        people = [[] for _ in range(40)]

        for i, hat in enumerate(hats):
            for person in hat:
                people[person-1].append(i)

        @lru_cache(None)
        def dfs(idx, mask):
            if idx >= len(people):
                return mask == 0
            ans = dfs(idx + 1, mask)
            for p in people[idx]:
                if (1 << p) & mask:
                    mask -= 1 << p
                    ans += dfs(idx + 1, mask)
                    mask += 1 << p
            return ans % mod

        return dfs(0, (1 << len(hats)) - 1)
