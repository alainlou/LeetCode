from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        @lru_cache(None)
        def dfs(start, end):
            if start >= end:
                return 0
            return max(nums[start] + dfs(start+2, end), dfs(start+1, end))

        return max(dfs(0, len(nums)-1), dfs(1, len(nums)))
