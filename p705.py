class MyHashSet:

    def __init__(self):
        self.dct = {}

    def add(self, key: int) -> None:
        self.dct[key] = True

    def remove(self, key: int) -> None:
        if key in self.dct:
            del self.dct[key]

    def contains(self, key: int) -> bool:
        return key in self.dct
