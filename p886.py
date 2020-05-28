from collections import defaultdict

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        colors = defaultdict(int)

        graph = defaultdict(set)

        for pair in dislikes:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])

        @lru_cache(None)
        def dfs(label, color):
            colors[label] = color
            for node in graph[label]:
                if node in colors and colors[node] == color:
                    return False
                elif node not in colors:
                    if not dfs(node, 1 if color == 0 else 0):
                        return False
            return True

        for i in range(1, N+1):
            if not dfs(i, colors[i]):
                return False

        return True
