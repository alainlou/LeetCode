class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [1, 1]+[0]*499
        for i in range(1, steps):
            cp = [0]*502
            cp[0] = dp[0]+dp[1]
            for j in range(1, min(i+2, arrLen)):
                cp[j] = dp[j-1]+dp[j]+dp[j+1]
            dp = cp
        return dp[0]%(10**9+7)