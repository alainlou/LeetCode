class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        mask = 1
        for i in range(31):
            if (x&mask)^(y&mask):
                distance += 1
            mask <<= 1
        return distance