class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo = float('inf')
        ans = 0

        for p in prices:
            if p < lo:
                lo = p
            else:
                ans = max(ans, p - lo)

        return ans
