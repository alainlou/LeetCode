class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = nums[:]
        right = nums[:]

        for i in range(1, len(nums)):
            left[i] *= left[i-1]
            right[-i-1] *= right[-i]

        left = [1] + left[:] + [1]
        right = [1] + right[:] + [1]

        ans = []

        for i in range(len(nums)):
            ans.append(left[i] * right[i+2])

        return ans
