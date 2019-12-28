class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[0,0] for i in range(n)] for j in range(n)]
        dp[0][0] = [0,1]
        dp[0][1] = [int(board[0][1]), 1] if board[0][1] != 'X' else [0,0]
        dp[1][0] = [int(board[1][0]), 1] if board[1][0] != 'X' else [0,0]
        for i in range(2, n):
            if board[0][i] != 'X' and dp[0][i-1] != [0,0]:
                dp[0][i] = [dp[0][i-1][0]+int(board[0][i]),1]
            if board[i][0] != 'X' and dp[i-1][0] != [0,0]:
                dp[i][0] = [dp[i-1][0][0]+int(board[i][0]),1]
        for i in range(1, n):
            for j in range(1, n):
                if board[i][j] == 'X':
                    dp[i][j] = [0,0]
                else:
                    maximum = 0
                    sq = [0,0]
                    if dp[i-1][j][0] > maximum:
                        maximum = dp[i-1][j][0]
                        sq = dp[i-1][j][:]
                    if dp[i][j-1][0] > maximum:
                        maximum = dp[i][j-1][0]
                        sq = dp[i][j-1][:]
                    elif dp[i][j-1][0] == maximum:
                        sq[1] += dp[i][j-1][1]
                    if dp[i-1][j-1][0] > maximum:
                        maximum = dp[i-1][j-1][0]
                        sq = dp[i-1][j-1][:]
                    elif dp[i-1][j-1][0] == maximum:
                        sq[1] += dp[i-1][j-1][1]
                    if sq != [0,0] and board[i][j] != 'S':
                        sq[0] += int(board[i][j])
                    dp[i][j] = sq
        dp[-1][-1][1] %= 10**9+7
        return dp[-1][-1]
