class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1,1]]*n
        ans = 0
        max_len = 0

        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0]+1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
            if dp[i][0] > max_len:
                max_len = dp[i][0]
                ans = dp[i][1]
            elif dp[i][0] == max_len:
                ans += dp[i][1]

        return ans if max_len > 1 else n
