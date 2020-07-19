class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == '1':
                l = 1
                i += 1
                while i < len(s) and s[i] == '1':
                    l += 1
                    i += 1
                ans += (l*(l+1))//2
                ans %= 10**9 + 7
            i += 1

        return ans
