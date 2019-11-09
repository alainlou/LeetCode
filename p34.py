class Solution:
    def binSearchLeft(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left == right:
            return left if nums[left] == target else -1
        elif left+1 == right:
            if nums[left] == target:
                return left
            return right if nums[right] == target else -1
        mid = (left+right)//2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
        return self.binSearchLeft(nums, target, left, right)
    
    def binSearchRight(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left == right:
            return right if nums[right] == target else -1
        elif left+1 == right:
            if nums[right] == target:
                return right
            return left if nums[left] == target else -1
        mid = (left+right)//2
        if nums[mid] > target:
            right = mid
        else:
            left = mid
        return self.binSearchRight(nums, target, left, right)
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        solution = [-1,-1]
        if len(nums) == 0:
            return solution
        n = len(nums)
        solution[0] = self.binSearchLeft(nums, target, 0, n-1)
        solution[1] = self.binSearchRight(nums, target, 0, n-1)
        return solution