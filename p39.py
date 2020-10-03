class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        curr = []

        def dfs(n, start):
            print(n, start)
            if n == 0:
                ans.append(curr[:])
                return
            if n < 0:
                return
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(n-candidates[i], i)
                curr.pop()

        dfs(target, 0)

        return ans
