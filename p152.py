class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        lo = nums[0] if nums[0] < 0 else None
        hi = nums[0] if nums[0] > 0 else None
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                tmp = hi
                hi = lo*nums[i] if lo else None
                lo = nums[i] if not tmp else nums[i]*tmp
            elif nums[i] == 0:
                lo, hi = 0, 0
            else:
                lo = lo*nums[i] if lo else None
                hi = nums[i] if not hi else nums[i]*hi
            ans = max(ans, nums[i])
            if hi:
                ans = max(ans, hi)

        return ans
