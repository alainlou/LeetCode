class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def solve(idx):
            if idx == n-1:
                return 0

            ans = float('inf')

            for dest in range(min(idx+nums[idx]+1, n) - 1, idx, -1):
                ans = min(ans, 1 + solve(dest))

            return ans

        return solve(0)
