class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def bfs(q, matrix, reach):
            while len(q) > 0:
                curr = q.pop(0)
                i = curr[0]
                j = curr[1]
                reach[i][j] = True
                if i > 0 and matrix[i-1][j] >= matrix[i][j] and not reach[i-1][j]:
                    q.append([i-1, j])
                if i < m-1 and matrix[i+1][j] >= matrix[i][j] and not reach[i+1][j]:
                    q.append([i+1, j])
                if j > 0 and matrix[i][j-1] >= matrix[i][j] and not reach[i][j-1]:
                    q.append([i, j-1])
                if j < n-1 and matrix[i][j+1] >= matrix[i][j] and not reach[i][j+1]:
                    q.append([i, j+1])
        m = len(matrix)
        if m == 0:
            return None
        n = len(matrix[0])
        reach_pacific = [[False]*n for _ in range(m)]
        reach_atlantic = [[False]*n for _ in range(m)]
        pacific_q = []
        atlantic_q = []
        for i in range(n):
            pacific_q.append([0, i])
            atlantic_q.append([m-1, i])
        for i in range(m):
            pacific_q.append([i, 0])
            atlantic_q.append([i, n-1])
        bfs(pacific_q, matrix, reach_pacific)
        bfs(atlantic_q, matrix, reach_atlantic)
        ans = []
        for i in range(m):
            for j in range(n):
                if reach_pacific[i][j] and reach_atlantic[i][j]:
                    ans.append([i, j])
        return ans
