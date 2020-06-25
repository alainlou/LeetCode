from collections import defaultdict
from heapq import heappush

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        can_reach = defaultdict(bool)
        can_reach[0] = True

        graph = defaultdict(set)
        for c in connections:
            graph[c[0]].add((c[1], True))
            graph[c[1]].add((c[0], False))

        visited = set()
        q = [(0, 0)]
        ans = 0

        while len(visited) < n:
            curr = q.pop(0)
            ans += curr[0]
            visited.add(curr[1])
            for dest in graph[curr[1]]:
                if dest[0] not in visited:
                    heappush(q, (1 if dest[1] else 0, dest[0]))

        return ans
