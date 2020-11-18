class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0:
            return 0

        orientation = [[2, 1],[None, 0]]

        curr = 0

        for _ in range(1, 1000000):
            curr += q
            if curr == p:
                return orientation[0][1]
            elif curr > p:
                curr %= p
                orientation[0], orientation[1] = orientation[1], orientation[0]
                orientation[0][0], orientation[0][1], orientation[1][0], orientation[1][1] = \
                orientation[0][1], orientation[0][0], orientation[1][1], orientation[1][0]
            elif curr < p:
                orientation[0][0], orientation[0][1], orientation[1][0], orientation[1][1] = \
                orientation[0][1], orientation[0][0], orientation[1][1], orientation[1][0]

        return None
