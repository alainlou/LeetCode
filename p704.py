class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        mid = (left+right)//2

        while left < right-1:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            mid = (left+right)//2

        return mid if mid < len(nums) and nums[mid] == target else -1
