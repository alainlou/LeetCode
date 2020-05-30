from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        n = len(grid)

        @lru_cache(None)
        def dfs(r1, c1, r2, c2):
            if r1 > n-1 or r2 > n-1 or c1 > n-1 or c2 > n-1 \
                or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == r2 == c1 == c2 == n-1:
                return grid[-1][-1]
            return (grid[r1][c1] if r1 == r2 and c1 == c2 else grid[r1][c1] + grid[r2][c2]) \
                    + max(dfs(r1+1, c1, r2+1, c2), dfs(r1+1, c1, r2, c2+1), dfs(r1, c1+1, r2+1, c2), dfs(r1, c1+1, r2, c2+1))

        return max(dfs(0, 0, 0, 0), 0)
