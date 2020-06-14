class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        nums.sort()
        dp = [[] for _ in range(len(nums))]
        dp[0] = [nums[0]]
        ans = dp[0]

        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i]%nums[j] == 0 and len(dp[j]) > len(dp[i]):
                    dp[i] = dp[j][:]
            dp[i].append(nums[i])
            if len(dp[i]) > len(ans):
                ans = dp[i]

        return ans
