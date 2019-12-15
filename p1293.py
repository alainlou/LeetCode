class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:        
        m = len(grid)
        n = len(grid[0])
        memo = {}
        visited = [[-1]*n for _ in range(m)]
        def solve(i, j, token):
            if i == m-1 and j == n-1:
                return 0
            visited[i][j] = token
            if (i, j, token) in memo:
                return memo[(i, j, token)]
            if grid[i][j] == 1:
                if token == 0:
                    return float('inf')
                token -= 1
            up = solve(i-1, j, token) if (i > 0 and visited[i-1][j] < token) else float('inf') 
            right = solve(i, j+1, token) if (j < n-1 and visited[i][j+1] < token) else float('inf')
            down = solve(i+1, j, token) if (i < m-1 and visited[i+1][j] < token) else float('inf') 
            left = solve(i, j-1, token) if (j > 0 and visited[i][j-1] < token) else float('inf')
            best = min(up, right, down, left)
            memo[(i, j, token)] = best
            return 1+best        
        ans = solve(0,0,k)
        return ans if ans != float('inf') else -1