from collections import defaultdict

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.memo = defaultdict(list)

        for j, p in enumerate(parent):
            self.memo[j].append(p)

        for i in range(1, 16):
            for j in range(len(parent)):
                if j == 0 or self.memo[j][-1] == -1:
                    self.memo[j].append(-1)
                else:
                    self.memo[j].append(self.memo[self.memo[j][-1]][i-1])

    def getKthAncestor(self, node: int, k: int) -> int:
        step = 15

        while k > 0:
            if node == -1:
                return -1
            if 1 << step > k:
                step -= 1
            else:
                node = self.memo[node][step]
                k -= 1 << step

        return node
