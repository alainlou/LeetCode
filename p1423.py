class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        if k >= n:
            return total

        rolling_sum = sum(cardPoints[:n-k])
        ans = total - rolling_sum

        for i in range(n-k, len(cardPoints)):
            rolling_sum += cardPoints[i]
            rolling_sum -= cardPoints[i-(n-k)]
            ans = max(ans, total - rolling_sum)

        return ans
