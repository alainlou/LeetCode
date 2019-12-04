class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [(i-1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i] = min(dp[i], 1+dp[j])
        return dp[n]