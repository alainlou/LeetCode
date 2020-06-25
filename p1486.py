class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        mask = 0

        for i in range(n):
            mask ^= start + 2*i

        return mask
