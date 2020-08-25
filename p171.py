class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0

        for i, c in enumerate(s):
            ans += 26**(len(s)-i-1) * (ord(c)-ord('A')+1)

        return ans
