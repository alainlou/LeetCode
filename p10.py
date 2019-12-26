class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        s = ' '+s[:]
        p = ' '+p[:]
        m = len(s)
        n = len(p)
        dp = [[False]*(n) for _ in range(m)]
        dp[0][0] = True
        for i in range(1, n):
            if p[i] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1, m):
            for j in range(1, n):
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    if dp[i][j-2]:
                        dp[i][j] = True
                    elif p[j-1] == '.' or p[j-1] == s[i]:
                        dp[i][j] = dp[i-1][j]
        return dp[m-1][n-1]