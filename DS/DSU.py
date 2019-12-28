class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, target):
        if self.parents[target] != target:
            self.parents[target] = self.find(self.parents[target])
        return self.parents[target]

    def union(self, child, parent):
        self.parents[child] = parent
