from collections import defaultdict
from functools import lru_cache

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        prereqs = defaultdict(set)

        for d in dependencies:
            prereqs[d[1]-1].add(d[0]-1)

        @lru_cache(None)
        def dfs(day, mask, left, pick_mask):
            if mask == 0:
                return day
            ans = float('inf')
            if left == 0:
                return dfs(day+1, mask - pick_mask, k, 0)
            else:
                picked = False
                for i in range(n):
                    if mask & (1 << i) and (not pick_mask & (1 << i)):
                        can_pick = True
                        # check all dependencies are zeroed
                        for d in prereqs[i]:
                            if mask & (1 << d):
                                can_pick = False
                                break
                        if can_pick:
                            ans = min(ans, dfs(day, mask, left-1, pick_mask + (1 << i)))
                            picked = True
                if not picked:
                    ans = min(ans, dfs(day+1, mask - pick_mask, k, 0))
            return ans

        return dfs(0, ((1 << (n))-1), k, 0)
