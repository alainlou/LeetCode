class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0 or len(board[0]) == 0:
            return

        def dfs(i, j):
            if board[i][j] != 'O':
                return
            board[i][j] = '.'
            if i > 0 and board[i-1][j] == 'O':
                dfs(i-1, j)
            if i < len(board) - 1 and board[i+1][j] == 'O':
                dfs(i+1, j)
            if j > 0 and board[i][j-1] == 'O':
                dfs(i, j-1)
            if j < len(board[0]) - 1 and board[i][j+1] == 'O':
                dfs(i, j+1)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)

        for i in range(len(board[0])):
            dfs(0, i)
            dfs(len(board)-1, i)

        for row in board:
            for i, c in enumerate(row):
                if c == '.':
                    row[i] = 'O'
                elif c == 'O':
                    row[i] = 'X'
