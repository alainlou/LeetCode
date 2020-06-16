class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.insert(0, float('inf'))
        left, right = 0, len(nums)
        mid = (left+right)//2

        while left != mid:
            if nums[mid] < target:
                left = mid
            else:
                right = mid
            mid = (left+right)//2

        return mid
