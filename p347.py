from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            heappush(arr, (-count[n], n))

        ans = []
        seen = set()
        for _ in range(k):
            curr = heappop(arr)
            while curr[1] in seen and len(arr) > 0:
                curr = heappop(arr)
            if curr[1] not in seen:
                ans.append(curr[1])
                seen.add(curr[1])

        return ans
