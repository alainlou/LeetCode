from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(lambda: defaultdict(int))

        for i, e in enumerate(edges):
            adj[e[0]][e[1]] = succProb[i]
            adj[e[1]][e[0]] = succProb[i]

        q = [(-1, start)]
        visited = set([start])
        probs = defaultdict(int)

        while len(q) > 0:
            prob, curr = heappop(q)
            prob = -prob

            visited.add(curr)
            probs[curr] = max(probs[curr], prob)

            for (node, p) in adj[curr].items():
                if node not in visited:
                    heappush(q, (-prob*p, node))

        return probs[end]
