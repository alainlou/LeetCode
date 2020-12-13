from functools import lru_cache
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(start, end):
            if start == end:
                return 0
            ans = float('-inf')
            left = nums[start-1] if start > 0 else 1
            right = nums[end] if end < n else 1
            if start+1 == end:
                return left*nums[start]*right
            for i in range(start, end):
                ans = max(ans, dfs(start, i) + left*nums[i]*right + dfs(i+1, end))
            return ans

        return dfs(0, n)
