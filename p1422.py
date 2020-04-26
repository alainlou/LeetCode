class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 1 if s[0] == '0' else 0
        ones = s[1:].count('1')
        ans = zeros + ones
        n = len(s)

        for c in range(1, n-1):
            if s[c] == '0':
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, zeros + ones)

        return ans
