class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count, col_count = [0]*m, [0]*n

        for i in range(m):
            for j in range(n):
                row_count[i] += mat[i][j]
                col_count[j] += mat[i][j]

        ans = 0

        for i in range(m):
            for j in range(n):
                ans += mat[i][j] if row_count[i] == 1 and col_count[j] == 1 else 0

        return ans
