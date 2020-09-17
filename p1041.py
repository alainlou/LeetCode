class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction, x, y = 0, 0, 0

        for i in instructions:
            if i == 'G':
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x += 1
                elif direction == 2:
                    y -= 1
                else:
                    x -= 1
            elif i == 'R':
                direction = (direction+1)%4
            else:
                direction = (4+direction-1)%4

        return (x, y) == (0, 0) or direction != 0
