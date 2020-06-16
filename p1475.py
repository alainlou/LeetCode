class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i, p in enumerate(prices):
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= p:
                    discount = prices[j]
                    break
            ans.append(p - discount)
        return ans
