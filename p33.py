class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = 0
        n = len(nums)
        left = 0
        right = n
        while left < right:
            mid = (left+right)//2
            if nums[mid-1] > nums[mid] and nums[mid] < nums[(mid+1)%n]:
                offset = mid
                break
            elif nums[left] < nums[mid]:
                left = mid
            else:
                right = mid
        left = offset
        right = n+offset
        while left < right:
            mid = (left+right)//2
            if nums[mid%n] == target:
                return mid%n
            elif nums[mid%n] < target:
                if left == mid:
                    return -1
                left = mid
            else:
                right = mid
        return -1