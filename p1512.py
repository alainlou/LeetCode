class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0

        for i, n  in enumerate(nums):
            for j in range(i+1, len(nums)):
                if n == nums[j] and i < j:
                    ans += 1

        return ans
