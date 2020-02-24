class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []

    def push(self, x: int) -> None:
        self.values.append(x)
        self.mins.append(x if len(self.mins) == 0 else min(x, self.mins[-1]))

    def pop(self) -> None:
        self.values.pop(-1)
        self.mins.pop(-1)

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[-1]
