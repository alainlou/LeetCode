import math

class Solution:
    def findComplement(self, num: int) -> int:
        l = int(math.log2(num)) if num > 0 else 0
        return num ^ ((1 << (l+1)) - 1)
