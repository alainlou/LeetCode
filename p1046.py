import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            n1 = heapq.heappop(stones)
            n2 = heapq.heappop(stones)
            if n1 != n2:
                heapq.heappush(stones, -abs(n1-n2))

        return 0 if len(stones) == 0 else -stones[0]
