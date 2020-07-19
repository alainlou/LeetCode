class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        lookup = [[0]*n for _ in range(m)]

        for i in range(n):
            lookup[0][i] = mat[0][i]
        for i in range(1, m):
            for j in range(n):
                lookup[i][j] = lookup[i-1][j] + 1 if mat[i][j] else 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    max_height = float('inf')
                    for k in range(j, -1, -1):
                        if lookup[i][k] > 0:
                            max_height = min(max_height, lookup[i][k])
                            ans += max_height
                        else:
                            break

        return ans
