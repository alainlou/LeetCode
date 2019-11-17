class Solution:
    def shift(self, grid: List[List[int]], n: int, m: int) -> List[List[int]]:
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m-1):
                result[i][j+1] = grid[i][j]
        result[0][0] = grid[n-1][m-1]
        for i in range(1, n):
            result[i][0] = grid[i-1][m-1]
        return result
        
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        while k > 0:
            grid = self.shift(grid, n, m)
            k -= 1
        return grid