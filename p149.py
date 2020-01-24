class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            if a == 0:
                return b
            if b == 0:
                return a
            return gcd(b, a%b)
        n = len(points)
        if n < 3:
            return n
        weight = {}
        for p in points:
            if (p[0], p[1]) not in weight:
                weight[(p[0], p[1])] = 1
            else:
                weight[(p[0], p[1])] += 1
        lines = {}
        for i in range(1, n):
            for j in range(i):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                g = gcd(dx, dy)
                slope = (dx/g, dy/g) if dx != 0 else float('inf')
                y_int = points[i][1] - slope[1]/slope[0]*points[i][0] if slope != float('inf') else str(points[i][0])
                if (slope, y_int) not in lines:
                    lines[(slope, y_int)] = set({(points[i][0], points[i][1]), (points[j][0], points[j][1])})
                else:
                    lines[(slope, y_int)].update({(points[i][0], points[i][1]), (points[j][0], points[j][1])})
        def process(x):
            ans = 0
            for i in x:
                ans += weight[i]
            return ans
        return max([process(x) for x in lines.values()])
