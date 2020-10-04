from collections import defaultdict
from numpy import arctan2, rad2deg

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        d = defaultdict(int)

        pre = 0

        for p in points:
            if p[0] == location[0] and p[1] == location[1]:
                pre += 1
            else:
                tmp = rad2deg(arctan2(p[1]-location[1], p[0]-location[0]))
                if tmp < 0:
                    tmp = 360+tmp
                d[tmp] += 1

        keys = sorted(list(d.keys()))
        left, right = 0, 1
        n = len(keys)
        curr = d[keys[0]]
        ans = curr

        def diff(a1, a2):
            if a2 >= a1:
                return a2-a1
            return 360+(a2-a1)

        while left < n and right <= 2*n:
            if diff(keys[left], keys[right%n-1]) <= angle and right-left < n+1:
                ans = max(ans, curr)
                if right < 2*n:
                    curr += d[keys[right%n]]
                    right += 1
                else:
                    curr -= d[keys[left]]
                    left += 1
            else:
                curr -= d[keys[left]]
                left += 1

        return pre+ans
