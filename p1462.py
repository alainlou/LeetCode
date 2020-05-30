from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        for pair in prerequisites:
            graph[pair[1]].add(pair[0])

        def bfs(start):
            visited = set()
            q = [start]
            while len(q) > 0:
                curr = q.pop(0)
                graph[start].add(curr)
                for dest in graph[curr]:
                    if dest not in visited:
                        q.append(dest)
                        visited.add(dest)

        for i in range(n):
            bfs(i)

        ans = []

        for q in queries:
            ans.append(q[0] in graph[q[1]] if q[0] != q[1] else False)

        return ans
