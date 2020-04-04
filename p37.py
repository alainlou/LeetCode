class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def possible(r, c, n):
            for i in range(9):
                if board[i][c] == n or board[r][i] == n:
                    return False

            for i in range((r//3)*3, (r//3)*3+3):
                for j in range((c//3)*3, (c//3)*3+3):
                    if board[i][j] == n:
                        return False

            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for n in range(1, 10):
                            if possible(i, j, str(n)):
                                board[i][j] = str(n)
                                if solve() == True:
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()
