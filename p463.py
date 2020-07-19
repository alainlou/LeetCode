class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def count(i, j):
            ret = 0
            if i-1 == -1 or grid[i-1][j] == 0:
                ret += 1
            if i+1 == m or grid[i+1][j] == 0:
                ret += 1
            if j-1 == -1 or grid[i][j-1] == 0:
                ret += 1
            if j+1 == n or grid[i][j+1] == 0:
                ret += 1
            return ret

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += count(i, j)

        return ans
