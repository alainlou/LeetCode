import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        visited = set()
        pq = []
        e = [0, [0]*m]
        for i in range(m):
            e[0] += mat[i][0]
        heapq.heappush(pq, e)

        while len(pq) > 0:
            e = heapq.heappop(pq)
            k -= 1
            if k == 0:
                return e[0]
            for i in range(m):
                if e[1][i] + 1 < len(mat[i]):
                    e[1][i] += 1
                    e[0] += mat[i][e[1][i]] - mat[i][e[1][i]-1]
                    if str(e[1]) not in visited:
                        heapq.heappush(pq, [e[0], e[1][:]])
                        visited.add(str(e[1]))
                    e[0] -= mat[i][e[1][i]] - mat[i][e[1][i]-1]
                    e[1][i] -= 1
