class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort(reverse=True)
        n = len(tokens)
        left, right = 0, n
        ans = 0

        while left < right:
            while left < right and P >= tokens[right-1]:
                P -= tokens[right-1]
                right -= 1
            ans = max(ans, n-right-left)
            if n-right-left == 0:
                break
            P += tokens[left]
            left += 1

        return ans
