from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(set)
        for t in times:
            graph[t[0]].add((t[2], t[1]))

        q = [(0, K)]
        distances = [float('inf')]*N
        visited = set()

        while len(q) != 0:
            curr = heappop(q)
            visited.add(curr[1])
            distances[curr[1]-1] = min(distances[curr[1]-1], curr[0])
            for adj in graph[curr[1]]:
                if adj[1] not in visited:
                    heappush(q, (curr[0]+adj[0], adj[1]))

        ans = max(distances)
        return ans if ans != float('inf') else -1
