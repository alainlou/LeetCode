from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if len(self.upper) == 0 or num > self.upper[0]:
            heappush(self.upper, num)
        else:
            heappush(self.lower, -num)

        if len(self.lower) > len(self.upper) + 1:
            heappush(self.upper, -heappop(self.lower))
        elif len(self.upper) > len(self.lower) + 1:
            heappush(self.lower, -heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper) and len(self.lower) > 0:
            return (-self.lower[0]+self.upper[0])/2
        return -self.lower[0] if len(self.lower) > len(self.upper) else self.upper[0]
