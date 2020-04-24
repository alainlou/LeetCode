import math

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        ans = m&n
        rng = n-m
        # flip up to msb of range
        msb = int(math.log2(rng))
        mask = ~((1 << (msb+1)) - 1)
        ans &= mask
        return ans
