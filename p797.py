class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        visited = [0]

        def dfs(idx):
            if idx == len(graph)-1:
                ans.append(visited[:])
                return
            for n in graph[idx]:
                if n not in visited:
                    visited.append(n)
                    dfs(n)
                    visited.pop()

        dfs(0)
        return ans
