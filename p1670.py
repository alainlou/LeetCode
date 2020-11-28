class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = []

    def pushFront(self, val: int) -> None:
        self.arr.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        idx = len(self.arr)//2
        self.arr.insert(idx, val)

    def pushBack(self, val: int) -> None:
        self.arr.append(val)

    def popFront(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr.pop(0)

    def popMiddle(self) -> int:
        if len(self.arr) == 0:
            return -1
        idx = len(self.arr)//2
        if len(self.arr)%2 == 0:
            idx -= 1
        return self.arr.pop(idx)

    def popBack(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr.pop(-1)
