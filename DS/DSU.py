class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, target):
        if self.parent[target] != target:
            self.parent[target] = self.find(self.parent[target])
        return self.parent[target]

    def union(self, c, p):
        self.parent[self.find(c)] = self.find(p)
