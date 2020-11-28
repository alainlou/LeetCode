from functools import lru_cache

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def make_decreasing(idx):
            if idx == 0:
                return 0
            ans = idx
            for i in range(1, idx+1):
                if nums[idx-i] < nums[idx]:
                    ans = min(ans, (i-1) + make_decreasing(idx-i))
            return ans
        
        @lru_cache(None)
        def make_increasing(idx):
            if idx == n-1:
                return 0
            ans = n-idx-1
            for i in range(idx+1, n):
                if nums[i] < nums[idx]:
                    ans = min(ans, (i-idx-1) + make_increasing(i))
            return ans
        
        ans = float('inf')
        
        for i in range(1, n-1):
            ans = min(ans, make_decreasing(i) + make_increasing(i))
        
        return ans