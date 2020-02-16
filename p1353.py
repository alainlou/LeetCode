from collections import defaultdict
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        by_day = defaultdict(list)
        last_day = float('-inf')
        for e in events:
            by_day[e[0]].append(e[1])
            last_day = max(last_day, e[1])

        heap = []
        day = 0
        ans = 0

        while day <= last_day:
            for e in by_day[day]:
                heapq.heappush(heap, e)
            while len(heap) > 0 and heap[0] < day:
                heapq.heappop(heap)
            if len(heap) > 0:
                heapq.heappop(heap)
                ans += 1
            day += 1

        return ans
