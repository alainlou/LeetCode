class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        m = 2 * (n - 1) + 1
        return (self.countOrders(n-1) * (m * (m+1)) // 2) % (10**9 + 7)
