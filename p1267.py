class Solution:        
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):            
            rowCount = 0
            locations = []
            for j in range(m):
                if grid[i][j] == 1:
                    rowCount += 1
                    locations.append(j)
            if rowCount > 1:
                for l in locations:
                    grid[i][l] = -1
                    count += 1
        for j in range(m):
            colCount = 0
            locations = []
            for i in range(n):
                if grid[i][j] != 0:
                    colCount += 1
                    locations.append(i)
            if colCount > 1:
                for l in locations:
                    if grid[l][j] == 1:
                        count += 1
        return count