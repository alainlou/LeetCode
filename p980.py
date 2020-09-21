class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        c = sum((row.count(0) for row in grid))
        visited = set()

        def dfs(i, j):
            if grid[i][j] == 2:
                return 1 if len(visited) > c else 0

            visited.add((i, j))
            ans = 0
            if i+1 < m and (i+1, j) not in visited and grid[i+1][j] != -1:
                ans += dfs(i+1, j)
            if i-1 >= 0 and (i-1, j) not in visited and grid[i-1][j] != -1:
                ans += dfs(i-1, j)
            if j+1 < n and (i, j+1) not in visited and grid[i][j+1] != -1:
                ans += dfs(i, j+1)
            if j-1 >= 0 and (i, j-1) not in visited and grid[i][j-1] != -1:
                ans += dfs(i, j-1)
            visited.remove((i, j))
            return ans

        start = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start.append(i)
                    start.append(j)
                    break

        return dfs(start[0], start[1])
