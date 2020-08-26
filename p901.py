class StockSpanner:

    def __init__(self):
        self.ranges = [(float('inf'), -1)]
        self.idx = 0

    def next(self, price: int) -> int:
        while self.ranges[0][0] <= price:
            del self.ranges[0]
        ret = self.idx - self.ranges[0][1]
        self.ranges.insert(0, (price, self.idx))
        self.idx += 1
        return ret
