class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)

        p = 31
        m = 10**9 + 7

        hash1 = 0
        hash2 = 0

        res = -1

        for i in range(n-1):
            hash1 += (ord(s[i])-97) * pow(p, i, m)
            hash1 %= m
            hash2 *= p
            hash2 += ord(s[~i])-97
            hash2 %= m
            if hash1 == hash2:
                res = i

        return s[:res+1]
