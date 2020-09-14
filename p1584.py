class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        distances = [[0]*m for _ in range(m)]

        if m < 2:
            return 0

        for i, p in enumerate(points):
            for j in range(i+1, m):
                d = abs(p[0]-points[j][0]) + abs(p[1]-points[j][1])
                distances[i][j] = d
                distances[j][i] = d

        visited = set()
        distance = [float('inf')]*m
        ans = 0
        curr = 0
        visited.add(0)

        while len(visited) < m:
            for i, d in enumerate(distances[curr]):
                distance[i] = min(distance[i], d)
            sel, lo = None, float('inf')
            for i, d in enumerate(distance):
                if d < lo and i not in visited:
                    sel = i
                    lo = d
            curr = sel
            ans += lo
            visited.add(curr)

        return ans
