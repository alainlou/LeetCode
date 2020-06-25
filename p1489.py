class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, target):
        if self.parent[target] != target:
            self.parent[target] = self.find(self.parent[target])
        return self.parent[target]

    def union(self, c, p):
        self.parent[self.find(c)] = p

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [[a, b, c, d] for d, (a, b, c) in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        crit = set()
        pseudo_crit = set()

        def mst(n, edges, start):
            if len(edges) == 0:
                return float('inf')
            dsu = DSU(n)
            dsu.union(edges[start][0], edges[start][1])
            cost = edges[start][2]
            for i, e in enumerate(edges):
                if dsu.find(e[0]) != dsu.find(e[1]):
                    dsu.union(e[0], e[1])
                    cost += e[2]
            for i in range(n):
                if dsu.find(i) != dsu.find(0):
                    return float('inf')
            return cost

        cost = mst(n, edges, 0)

        for i, e in enumerate(edges):
            tmp = edges.pop(i)
            if mst(n, edges, 0) > cost:
                crit.add(e[3])
            edges.insert(i, tmp)
            if mst(n, edges, i) == cost:
                pseudo_crit.add(e[3])

        return [list(crit), list(pseudo_crit-crit)]
