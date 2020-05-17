class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0]*(n) for _ in range(n)]
        dp[0][0] = arr[0]

        for i in range(1, n):
            dp[0][i] = dp[0][i-1] ^ arr[i]

        for i in range(1, n):
            dp[i][i] = arr[i]
            for j in range(i+1, n):
                dp[i][j] = dp[i][j-1] ^ arr[j]

        ans = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    if dp[i][j-1] == dp[j][k]:
                        ans += 1

        return ans
