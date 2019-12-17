class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        board = [[False]*n for _ in range(n)]
        
        def valid(board, i, j):
            for k in range(n):
                if k != i and board[k][j]:
                    return False
            for k in range(-min(i, j), min(n-i-1, n-j-1)):
                if k != 0 and board[i+k][j+k]:
                    return False
            for k in range(-min(i, n-j-1), min(n-i-1, j)):
                if k != 0 and board[i+k][j-k]:
                    return False
            return True
                
        def recurse(board, row):
            if row > len(board) - 1:
                self.count += 1
                return
            for i in range(n):
                board[row][i] = True
                if valid(board, row, i):
                    recurse(board, row+1)
                board[row][i] = False
                
        recurse(board, 0)
        
        return self.count