import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                heapq.heappush(heap, matrix[i][j])
        for i in range(k-1):
            heapq.heappop(heap)
        return heap[0]
