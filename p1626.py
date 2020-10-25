from functools import lru_cache

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = []
        for i, s in enumerate(scores):
            arr.append((ages[i], s))
        arr.sort()

        @lru_cache(None)
        def dfs(idx):
            if idx > len(arr)-1:
                return 0
            ans = arr[idx][1]
            for i in range(idx+1, len(arr)):
                if arr[i][1] >= arr[idx][1]:
                    ans = max(ans, arr[idx][1]+dfs(i))
            return ans

        ans = 0

        for i in range(len(arr)):
            ans = max(ans, dfs(i))

        return ans
