class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n
        mid = (lo+hi)//2

        while lo != mid:
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                return nums[mid]
            if nums[mid-1] == nums[mid]:
                if mid%2 == 0:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if mid%2 == 0:
                    lo = mid+2
                else:
                    hi = mid
            mid = (lo+hi)//2

        return nums[mid]
