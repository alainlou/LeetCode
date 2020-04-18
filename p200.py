class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0

        if m == 0 or n == 0:
            return 0

        def fill(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            fill(i, j+1)
            fill(i, j-1)
            fill(i+1, j)
            fill(i-1, j)

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    fill(i, j)

        return ans
