from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])

        neighbours = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for k in range(max(0, i-1), min(m, i+2)):
                    for l in range(max(0, j-1), min(n, j+2)):
                        if not (k == i and l == j) and board[k][l]:
                            neighbours[i][j] += 1


        for i in range(m):
            for j in range(n):
                if (board[i][j] and not 2 <= neighbours[i][j] <= 3) or \
                (not board[i][j] and neighbours[i][j] == 3):
                    board[i][j] = 0 if board[i][j] else 1
