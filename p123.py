class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        left, right = [], []
        lo, hi = float('inf'), float('-inf')

        for p in prices:
            if p < lo:
                lo = p
                hi = float('-inf')
                left.append(left[-1] if len(left) > 0 else 0)
            else:
                hi = max(hi, p)
                left.append(hi-lo)

        lo, hi = float('inf'), float('-inf')

        for i in range(n-1, -1, -1):
            if prices[i] > hi:
                hi = prices[i]
                lo = float('inf')
                right.insert(0, right[0] if len(right) > 0 else 0)
            else:
                lo = min(lo, prices[i])
                right.insert(0, hi-lo)

        ans = left[-1]

        for i in range(n-1):
            ans = max(ans, left[i] + right[i+1])

        return ans
