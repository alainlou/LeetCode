class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for idx in range(32):
            bit = ((1 << idx)&n) >> (idx)
            ans <<= 1
            ans += bit

        return ans
