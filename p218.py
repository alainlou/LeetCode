import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        pq = [0]
        for i in range(len(buildings)):
            b = buildings.pop(0)
            buildings.append([True, b[0], -b[2]])
            buildings.append([False, b[1], -b[2]])
        buildings.sort(key=lambda x:x[1])
        minimum = float('inf')
        for b in buildings:
            if b[0]:
                if b[2] < minimum:
                    minimum = b[2]
                    if len(ans) > 0 and ans[-1][0] == b[1]:
                        ans[-1][1] = max(ans[-1][1], -b[2])
                    else:
                        ans.append([b[1], -b[2]])
                heapq.heappush(pq, b[2])
            else:
                tmp = pq[0]
                pq.remove(b[2])
                heapq.heapify(pq)
                if pq[0] > tmp:
                    minimum = pq[0]
                    if len(ans) > 0 and ans[-1][0] == b[1]:
                        ans[-1][1] = min(ans[-1][1], -pq[0])
                    else:
                        ans.append([b[1], -pq[0]])
        for i in range(len(ans)):
            while i < len(ans) and ans[i][1] == ans[i-1][1]:
                del ans[i]
        return ans