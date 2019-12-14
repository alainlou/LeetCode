class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        
        if n == 1:
            return arr[0][0]
        
        dp = [row[:] for row in arr]
        left = [float('inf')]*n
        right = [float('inf')]*n
        best = [float('inf')]*n
        
        for i in range(n-2, -1, -1):
            
            for j in range(1, n):
                left[j] = min(left[j-1], dp[i+1][j-1])
            
            for j in range(n-2, -1, -1):
                right[j] = min(right[j+1], dp[i+1][j+1])
                
            best[0] = right[0]
            
            for j in range(1, n-1):
                best[j] = min(left[j], right[j])
                
            best[-1] = left[-1]
            
            for j in range(n):
                dp[i][j] += best[j]
                
            left = [float('inf')]*n
            right = [float('inf')]*n
            best = [float('inf')]*n
        
        return min(dp[0])