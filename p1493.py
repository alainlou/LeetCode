class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = [0]*len(nums)
        left[1] = nums[0]
        right = [0]*len(nums)
        right[-2] = nums[-1]

        for i in range(2, len(nums)):
            left[i] = left[i-1] + 1 if nums[i-1] == 1 else 0
        for i in range(len(nums)-3, -1, -1):
            right[i] = right[i+1] + 1 if nums[i+1] == 1 else 0

        ans = 0
        for i in range(len(left)):
            ans = max(ans, left[i]+right[i])

        return ans
