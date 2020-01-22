class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        memo = {}
        def process(s, i):
            if i >= len(s):
                return 1
            elif i in memo:
                return memo[i]
            elif s[i] == '0':
                return 0
            ans = process(s, i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                ans += process(s, i+2)
            memo[i] = ans
            return ans
        return process(s, 0)
