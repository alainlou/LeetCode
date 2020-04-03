class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr = 0

        for n in nums:
            curr += n
            ans = max(curr, ans)
            curr = max(curr, 0)

        return ans
