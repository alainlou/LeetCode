class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)+1
        n = len(s)+1
        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True
        for i in range(1, n):
            dp[0][i] = False
        for i in range(1, m):
            if p[i-1] == '*':
                dp[i][0] = dp[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if p[i-1] == '?' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]
