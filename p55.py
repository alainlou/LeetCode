class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        furthest = 0

        for i, n in enumerate(nums):
            if i <= furthest:
                furthest = max(furthest, i+n)
            else:
                return False

        return furthest >= n-1
