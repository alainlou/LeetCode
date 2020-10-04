class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b, self.m, self.s = big, medium, small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.b -= 1
            return self.b >= 0
        if carType == 2:
            self.m -= 1
            return self.m >= 0
        self.s -= 1
        return self.s >= 0
