class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left != right:
                if nums[i] + nums[left] + nums[right] == 0:
                    if len(ans) == 0 or [nums[i], nums[left], nums[right]] != ans[-1]:
                        ans.append([nums[i], nums[left], nums[right]])
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return ans
