import math

class Solution:
    def execute(self, nums, divisor):
        ans = 0
        for n in nums:
            ans += math.ceil(n/divisor)
        return ans
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo = max(sum(nums)//threshold, 1)
        hi = 1000000
        mid = (lo+hi)//2
        while hi > lo+1:
            if self.execute(nums, mid) <= threshold:
                hi = mid
            else:
                lo = mid
            mid = (lo+hi)//2
        if self.execute(nums, lo) <= threshold:
            return lo
        return hi