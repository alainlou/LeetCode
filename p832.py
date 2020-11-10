class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        for i, row in enumerate(A):
            A[i] = row[::-1]
        for i in range(m):
            for j in range(n):
                A[i][j] = 0 if A[i][j] == 1 else 1
        return A
