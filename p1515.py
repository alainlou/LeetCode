from math import sqrt

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        x, y = 50, 50

        for _ in range(1000):
            top_x, top_y, denom = 0, 0, 0
            for p in positions:
                dist = max(sqrt((p[0]-x)**2 + (p[1]-y)**2), 1e-10)
                top_x += (p[0]/dist)
                top_y += (p[1]/dist)
                denom += (1/dist)

            x, y = top_x/denom, top_y/denom

        return sum(sqrt((p[0]-x)**2 + (p[1]-y)**2) for p in positions)
