from functools import lru_cache

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @lru_cache(None)
        def dfs(idx1, idx2, flag):
            if idx1 >= len(nums1) or idx2 >= len(nums2):
                return 0 if flag else float('-inf')

            return max(nums1[idx1]*nums2[idx2] + dfs(idx1+1, idx2+1, True), dfs(idx1+1, idx2, flag), dfs(idx1, idx2+1, flag))

        return dfs(0, 0, False)
