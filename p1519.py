from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        connections = defaultdict(list)

        for e in edges:
            connections[e[0]].append(e[1])
            connections[e[1]].append(e[0])

        counts = defaultdict(lambda: [0]*26)

        visited = set({0})

        def dfs(idx):
            for c in connections[idx]:
                if c not in visited:
                    visited.add(c)
                    dfs(c)
                    for i in range(26):
                        counts[idx][i] += counts[c][i]
                    visited.remove(c)
            counts[idx][ord(labels[idx])-ord('a')] += 1

        dfs(0)

        ans = []

        for i in range(n):
            ans.append(counts[i][ord(labels[i])-ord('a')])

        return ans
