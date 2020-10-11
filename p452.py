class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))

        ans = 0
        idx = 0
        n = len(points)

        while idx < n:
            end = points[idx][1]
            idx += 1
            while idx < n and points[idx][0] <= end:
                end = min(end, points[idx][1])
                idx += 1
            ans += 1

        return ans
