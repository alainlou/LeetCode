class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]

        if dx == 0:
            for c in coordinates:
                if c[0] != coordinates[0][0]:
                    return False
            return True

        slope = dy/dx

        for i in range(2, len(coordinates)):
            dy = coordinates[i][1] - coordinates[0][1]
            dx = coordinates[i][0] - coordinates[0][0]
            if dx == 0 or dy/dx != slope:
                return False

        return True
