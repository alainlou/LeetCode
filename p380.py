from random import randrange

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        self.arr[len(self.arr)-1], self.arr[idx] = self.arr[idx], self.arr[len(self.arr)-1]
        self.map[self.arr[idx]] = idx
        del self.map[val]
        del self.arr[-1]
        return True

    def getRandom(self) -> int:
        return self.arr[randrange(0, len(self.arr))]
