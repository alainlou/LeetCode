import random

class Solution:

    def __init__(self, w: List[int]):
        self.weights = [0]
        n = sum(w)
        for e in w:
            self.weights.append(self.weights[-1] + e/n)
        del self.weights[-1]

    def pickIndex(self) -> int:
        left = 0
        right = len(self.weights)
        mid = (left+right)//2
        target = random.random()

        while left != mid:
            if self.weights[mid] < target:
                left = mid
            else:
                right = mid
            mid = (left+right)//2

        return mid
