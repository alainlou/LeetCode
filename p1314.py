class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0]*n for row in mat]
        window = 0
        for i in range(K+1):
            for j in range(K+1):
                window += mat[i][j] if i < m and j < n else 0
        ans[0][0] = window
        for i in range(m):
            top = 0
            if i-K-1 >= 0:
                for k in range(min(n, K+1)):
                    top += mat[i-K-1][k]
            bottom = 0
            if i+K < m:
                for k in range(min(n, K+1)):
                    bottom += mat[i+K][k]
            ans[i][0] = ans[i-1][0] + bottom - top if i != 0 else ans[0][0]
            for j in range(1, n):
                right = 0
                if j+K < n:
                    for k in range(max(0, i-K), min(m, i+K+1)):
                        right += mat[k][j+K]
                left = 0
                if j-K-1 >= 0:
                    for k in range(max(0, i-K), min(m, i+K+1)):
                        left += mat[k][j-K-1]
                ans[i][j] = ans[i][j-1] + right - left
        return ans
                