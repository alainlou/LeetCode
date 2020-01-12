class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        mask = 1
        m = max(a, b, c)
        while mask <= m:
            if c&mask:
                if a&mask == 0 and b&mask == 0:
                    ans += 1
            else:
                if a&mask:
                    ans += 1
                if b&mask:
                    ans += 1
            mask <<= 1
        return ans
