from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row, pos1, pos2):
            if row > m-1:
                return 0
            if pos1 < 0 or pos2 < 0 or pos1 > n-1 or pos2 > n-1:
                return float('-inf')
            return grid[row][pos1] if pos1 == pos2 else (grid[row][pos1] + grid[row][pos2]) \
                    + max(dfs(row+1, pos1-1, pos2-1), dfs(row+1, pos1, pos2-1), dfs(row+1, pos1+1, pos2-1), \
                    dfs(row+1, pos1-1, pos2), dfs(row+1, pos1, pos2), dfs(row+1, pos1+1, pos2), \
                    dfs(row+1, pos1-1, pos2+1), dfs(row+1, pos1, pos2+1), dfs(row+1, pos1+1, pos2+1))

        return dfs(0, 0, n-1)
