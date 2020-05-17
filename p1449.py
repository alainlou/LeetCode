class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        ans = 0
        dp = [None]*(target+1)
        dp[0] = 0

        for i in range(1, target+1):
            for j, c in enumerate(cost):
                if i - c >= 0 and dp[i-c] is not None:
                    dp[i] = max(dp[i] if dp[i] is not None else 0, dp[i-c]*10 + (j+1))

        return str(dp[-1]) if dp[-1] is not None else '0'
