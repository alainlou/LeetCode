from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(idx):
            if idx >= n:
                return 0
            return max(dfs(idx+1), nums[idx]+dfs(idx+2))

        return dfs(0)
