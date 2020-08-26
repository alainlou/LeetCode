import math

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        l = int(math.log2(N)) if N > 0 else 0
        return N ^ ((1 << (l+1)) - 1)
