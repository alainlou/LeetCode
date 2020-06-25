class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        ans = 0
        for i in range(0, n):
            ans += self.numTrees(i) * self.numTrees(n-i-1)
        return ans
