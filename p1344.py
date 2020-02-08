class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ang1 = hour/12*360+minutes/60*360/12
        ang2 = minutes/60*360
        return min(abs(ang1-ang2), 360-abs(ang1-ang2))
