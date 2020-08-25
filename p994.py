class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j):
            if grid[i][j] == 2:
                return 0
            if grid[i][j] == 1:
                ret = float('inf')
                visited.add((i, j))
                if i-1 >= 0 and (i-1, j) not in visited:
                    ret = min(ret, 1+dfs(i-1, j))
                if i+1 < m and (i+1, j) not in visited:
                    ret = min(ret, 1+dfs(i+1, j))
                if j-1 >= 0 and (i, j-1) not in visited:
                    ret = min(ret, 1+dfs(i, j-1))
                if j+1 < n and (i, j+1) not in visited:
                    ret = min(ret, 1+dfs(i, j+1))
                visited.remove((i, j))
                return ret
            return float('inf')

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans if ans != float('inf') else -1
