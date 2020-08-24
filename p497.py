from random import randint

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        self.total_weight = 0
        for i, r in enumerate(rects):
            self.weights.append(((r[3]-r[1]+1)*(r[2]-r[0]+1)))
            self.total_weight += ((r[3]-r[1]+1)*(r[2]-r[0]+1))

    def pick(self) -> List[int]:
        w = randint(0, self.total_weight)
        incr = 0
        idx = 0
        while incr < w:
            incr += self.weights[idx]
            idx += 1
        idx -= 1
        r = self.rects[idx]
        return [randint(r[0], r[2]), randint(r[1], r[3])]
