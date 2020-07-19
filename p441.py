class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 1

        while n >= 0:
            n -= ans
            ans += 1

        return ans-2
