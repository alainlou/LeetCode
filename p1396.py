from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.start = {}
        self.times = defaultdict(int)
        self.counts = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.start[id]
        time = t - start[0]
        self.times[(start[1], stationName)] += time
        self.counts[(start[1], stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.times[(startStation, endStation)]/self.counts[(startStation, endStation)]
