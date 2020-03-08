class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        count = 0
        right = float('-inf')
        bitmask = 0

        for l in light:
            l -= 1
            right = max(right, l)
            bitmask += 1 << l
            if (1 << (right + 1)) - 1 == bitmask:
                count += 1

        return count
