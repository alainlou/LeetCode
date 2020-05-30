from heapq import heappop, heappush
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        min_heap = []
        ans = []

        for p in points:
            heappush(min_heap, (sqrt(p[0]**2 + p[1]**2), p))

        for i in range(K):
            ans.append(heappop(min_heap)[1])

        return ans
