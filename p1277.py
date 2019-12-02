class Solution:
    def expand(self, matrix, r, c, s):
        if r+s >= len(matrix) or c+s >= len(matrix[0]):
            return s
        for i in range(s+1):
            if not (matrix[r+s][c+i] == 1 and matrix[r+i][c+s] == 1):
                return s                
        return self.expand(matrix, r, c, s+1)
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    ans += self.expand(matrix, i, j, 1)
        return ans