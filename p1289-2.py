class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0][0]
        dp = [row[:] for row in arr]
        left = [float('inf')]*n
        for i in range(n-2, -1, -1):            
            for j in range(1, n):
                left[j] = min(left[j-1], dp[i+1][j-1])
            dp[i][-1] += left[-1]
            right = dp[i+1][-1]
            for j in range(n-2, -1, -1):
                dp[i][j] += min(left[j], right)
                right = min(right, dp[i+1][j])
            left = [float('inf')]*n
        return min(dp[0])