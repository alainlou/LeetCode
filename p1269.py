class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [1] + [0] * (steps+1)
        for i in range(steps):
            cp = dp[:]
            for j in range(i+2):
                cp[j] = dp[j-1]+dp[j]
                if j+1 < arrLen:
                    cp[j] += dp[j+1]
            dp = cp
        return dp[0]%(10**9+7)