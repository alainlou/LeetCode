from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = defaultdict(lambda: defaultdict(lambda: float('inf')))

        for i in range(m*n):
            dist[i][i] = 0

        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dist[i*n+j][(i-1)*n+j] = abs(heights[i][j]-heights[i-1][j])
                    dist[(i-1)*n+j][i*n+j] = abs(heights[i][j]-heights[i-1][j])
                if i+1 < m:
                    dist[i*n+j][(i+1)*n+j] = abs(heights[i][j]-heights[i+1][j])
                    dist[(i+1)*n+j][i*n+j] = abs(heights[i][j]-heights[i+1][j])
                if j-1 >= 0:
                    dist[i*n+j][i*n+j-1] = abs(heights[i][j]-heights[i][j-1])
                    dist[i*n+j-1][i*n+j] = abs(heights[i][j]-heights[i][j-1])
                if j+1 < n:
                    dist[i*n+j][i*n+j+1] = abs(heights[i][j]-heights[i][j+1])
                    dist[i*n+j+1][i*n+j] = abs(heights[i][j]-heights[i][j+1])

        curr = (0, 0)
        pq = [(0, 0)]
        visited = set()
        while len(visited) < m*n:
            while curr[1] in visited:
                curr = heappop(pq)
            visited.add(curr[1])
            dist[0][curr[1]] = curr[0]
            for node in dist[curr[1]]:
                if node not in visited:
                    heappush(pq, (max(curr[0], dist[curr[1]][node]), node))


        return dist[0][m*n-1]
