class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        n = 0

        for c in S:
            if c.isdigit():
                n *= int(c)
            else:
                n += 1

        for c in reversed(S):
            K %= n

            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                n /= int(c)
            else:
                n -= 1
