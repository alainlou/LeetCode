class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1:
            return 1 if nums[0] < k else 0

        left, right = 0, 1
        curr = nums[0]
        ans = 1 if nums[0] < k else 0

        while right < n:
            curr *= nums[right]
            right += 1
            while curr >= k and left < right:
                curr //= nums[left]
                left += 1
            ans += right-left

        return ans
