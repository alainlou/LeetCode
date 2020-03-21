class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1

        while idx < len(nums) - 1:
            if nums[idx-1] == nums[idx] == nums[idx+1]:
                del nums[idx]
            else:
                idx += 1

        return len(nums)
