class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        ans = 0

        def fill(row, col):
            if row >= m or row < 0 or col >= n or col < 0:
                return
            board[row][col] = '.'
            if row+1 < m and board[row+1][col] == 'X':
                fill(row+1, col)
            if row-1 >= 0 and board[row-1][col] == 'X':
                fill(row-1, col)
            if col+1 < n and board[row][col+1] == 'X':
                fill(row, col+1)
            if col-1 >= 0 and board[row][col-1] == 'X':
                fill(row, col-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    fill(i, j)
                    ans += 1

        return ans
