class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        n = len(nums)

        while idx < n:
            if nums[idx] == 0:
                del nums[idx]
                nums.append(0)
                n -= 1
            else:
                idx += 1
