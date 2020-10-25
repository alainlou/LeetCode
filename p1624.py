class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        n = len(s)

        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    ans = max(ans, j-i-1)

        return ans
