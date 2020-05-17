from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        beside = defaultdict(list)
        parent = {}
        targets = []

        for i, a in enumerate(hasApple):
            if a == True:
                targets.append(i)

        for e in edges:
            beside[e[0]].append(e[1])
            beside[e[1]].append(e[0])

        visited = set()
        # bfs from 0
        q = [(0, 0)]
        while len(q) > 0:
            curr = q.pop(0)
            parent[curr[0]] = curr[1]
            for node in beside[curr[0]]:
                if node not in visited:
                    q.append((node, curr[0]))
                    visited.add(node)

        paths = set()
        for t in targets:
            if t == 0:
                continue
            curr = t
            while curr != 0:
                paths.add((curr, parent[curr]))
                paths.add((parent[curr], curr))
                curr = parent[curr]

        return len(paths)
